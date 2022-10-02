from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from .models import LogoModel


def render_to_pdf(template_src, context_data={}):
    template = get_template(template_src)
    html = template.render(context_data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), 'application/pdf')
    return None


data = {
    "company": "Al-jabr texnopark",
    "address": "Unversitet ko'chasi 4-uy",
    "city": "Tashkent",
    "zipcode": "123123",
    "phone": "71 123-45-67",
    "email": "al-jabr@gmail.com",
    "website": "al-jabr.uz"
}


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        # pdf = render_to_pdf('pdf_template.html', data)
        # pk = kwargs.get('pk')
        # user = get_object_or_404(User, pk=pk)

        template_path = 'pdf_template.html'
        context = {'logo': LogoModel.objects.get(id=1)}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')

        # to directly download the pdf we need attachment
        # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # to view on browser we can remove attachment
        response['Content-Disposition'] = 'filename="report.pdf"'

        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
        # return HttpResponse(pdf, 'application/pdf')


class DownloadPDF(View):

    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("123123")
        content = "attachment; filename='%s'" % (filename)
        response["Content-Dispostion"] = content
        return response


def main_view(request):
    context = {}
    return render(request, 'index.html', context)
