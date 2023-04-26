from django.views.generic import DetailView

from .models import MagazineDepartment
import io
from django.http import HttpResponse
import fitz


class MagazineDepartmentDetail(DetailView):
    model = MagazineDepartment
    context_object_name = "department"

    template_name = "magazine/magazine_department_detail.html"

# def serve_pdf(request, pdf_document_id):
#     # Retrieve the PDF document from the database
#     pdf_document = Document.objects.get(id=pdf_document_id)
#
#     # Open the PDF document with PyMuPDF
#     doc = fitz.open(pdf_document.file.path)
#
#     # Render the first page of the PDF as a PNG image
#     page = doc[0]
#     pix = page.get_pixmap(alpha=False)
#     img_bytes = io.BytesIO(pix.image_data)
#
#     # Serve the image in a Django response
#     response = HttpResponse(content_type='image/png')
#     response['Content-Disposition'] = 'inline; filename=image.png'
#     img_bytes.seek(0)
#     response.write(img_bytes.read())
#     return response
