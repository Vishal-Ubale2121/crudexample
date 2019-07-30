from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from employee.views import MyForm,Home_View,ShowTable,Delete,Upload_File,Model_Form,Formset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', MyForm.as_view()),
    path('upload', Model_Form.as_view()),
    path('show',ShowTable.as_view()),
    path('json',Upload_File.as_view()),
    path('formset',Formset.as_view()),
    path('delete/<int:id>', Delete.as_view()),
    path('navbar', Upload_File.navbar),
    path('', Home_View.as_view()),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)