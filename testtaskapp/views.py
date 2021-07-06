from django.shortcuts import render
from .models import Theme

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def index(request):
    themes = Theme.objects.all()
    return render(request, 'index.html', {'themes' : themes})


def save_pdf(request):
    if request.method == 'POST':
        selectedThemesID = request.POST.getlist('selectedThemes')
        selectedThemes = Theme.objects.filter(pk__in=selectedThemesID)

        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

        textob = c.beginText()
        textob.setTextOrigin(inch,inch)
        textob.setFont('Helvetica',14)

        lines=[]

        for theme in selectedThemes:
            lines.append("->  " + theme.title)
            lines.append(theme.url)
            lines.append(" ")

        for line in lines:
            textob.textLine(line)

        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='themes.pdf')