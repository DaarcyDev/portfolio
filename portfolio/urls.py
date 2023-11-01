
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
    path("DaarcyDevAdmin/Crud/About/Create",views.crudAboutCreate, name="crudAboutCreate"),

    path("DaarcyDevAdmin/Crud/Project",views.crudProject, name="crudProject"),
    path("DaarcyDevAdmin/Crud/Project/Create",views.crudProjectCreate, name="crudProjectCreate"),
    path("DaarcyDevAdmin/Crud/Project/Update/<int:pk>",views.crudProjectUpdate, name="crudProjectUpdate"),
    path("DaarcyDevAdmin/Crud/Project/Delete/<int:pk>", views.crudProjectDelete, name="crudProjectDelete"),


    path("DaarcyDevAdmin/Crud/Skill",views.crudSkill, name="crudSkill"),
    path("DaarcyDevAdmin/Crud/Skill/Create",views.crudSkillCreate, name="crudSkillCreate"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)