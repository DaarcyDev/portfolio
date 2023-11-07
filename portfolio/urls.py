
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
    path('DaarcyDevAdmin/Crud/About/Update/<int:pk>/', views.crudAboutUpdate, name='crudAboutUpdate'),
    path("DaarcyDevAdmin/Crud/About/Delete/<int:pk>", views.crudAboutDelete, name="crudAboutDelete"),

    path("DaarcyDevAdmin/Crud/Project",views.crudProject, name="crudProject"),
    path("DaarcyDevAdmin/Crud/Project/Create",views.crudProjectCreate, name="crudProjectCreate"),
    path("DaarcyDevAdmin/Crud/Project/Update/<int:pk>",views.crudProjectUpdate, name="crudProjectUpdate"),
    path("DaarcyDevAdmin/Crud/Project/Delete/<int:pk>", views.crudProjectDelete, name="crudProjectDelete"),

    path("DaarcyDevAdmin/Crud/Skill",views.crudSkill, name="crudSkill"),
    path("DaarcyDevAdmin/Crud/Skill/Create",views.crudSkillCreate, name="crudSkillCreate"),
    path("DaarcyDevAdmin/Crud/Skill/Update/<int:pk>",views.crudSkillUpdate, name="crudSkillUpdate"),
    path("DaarcyDevAdmin/Crud/Skill/Delete/<int:pk>",views.crudSkillDelete, name="crudSkillDelete"),

    path("DaarcyDevAdmin/Crud/Blog",views.crudBlog, name="crudBlog"),
    path("DaarcyDevAdmin/Crud/Blog/Create",views.crudBlogCreate, name="crudBlogCreate"),
    path("DaarcyDevAdmin/Crud/Blog/Update/<int:pk>",views.crudBlogUpdate, name="crudBlogUpdate"),
    path("DaarcyDevAdmin/Crud/Blog/Delete/<int:pk>",views.crudBlogDelete, name="crudBlogDelete"),

    path("DaarcyDevAdmin/Crud/Contact",views.crudContact, name="crudContact"),
    path("DaarcyDevAdmin/Crud/Contact/Create",views.crudContactCreate, name="crudContactCreate"),
    path('DaarcyDevAdmin/Crud/Contact/Update/<int:pk>/', views.crudContactUpdate, name='crudContactUpdate'),
    path("DaarcyDevAdmin/Crud/Contact/Delete/<int:pk>", views.crudContactDelete, name="crudContactDelete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

