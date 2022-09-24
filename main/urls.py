from django.urls import path
from .views import main_view, ViewPDF, DownloadPDF
urlpatterns = [
    path('', main_view),
    path('pdf_view/', ViewPDF.as_view(), name='view_pdf'),
    path('pdf_download/', DownloadPDF.as_view(), name='download_pdf')
]