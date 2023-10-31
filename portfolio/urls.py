
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index, name="index"),
    path("DaarcyDevAdmin/",views.DaarcyDevAdmin, name="admin"),
    path("DaarcyDevAdmin/Crud/",views.crud, name="crud"),
    path("DaarcyDevAdmin/Crud/About",views.crudAbout, name="crudAbout"),
    path("DaarcyDevAdmin/Crud/Project",views.crudProject, name="crudProject"),
    path("DaarcyDevAdmin/Crud/Project/Create",views.crudProjectCreate, name="crudProjectCreate"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)