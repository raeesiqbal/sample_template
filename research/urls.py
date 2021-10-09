from django.urls import path
from . import views

urlpatterns = [

    path("researchhub/", views.research, name="research"),
    path("researchdetail/<int:id>", views.research_detail, name="research_detail"),
    path("ajax", views.ajax, name="ajax"),
    path("addresearch/", views.add_research, name="add_research"),
    path("saveresearch/", views.save_research, name="save_research"),
    path("editresearch/<int:id>", views.edit_research, name="edit_research"),
    path("saveeditresearch/<int:id>", views.save_edit_research, name="save_edit_research"),
    path("deleteresearch/<int:id>", views.delete_research, name="delete_research"),
    path("relatedidea", views.related_idea, name="related_idea"),
    path("dropidea", views.drop_idea, name="drop_idea"),
    path("saveidea", views.save_idea, name="save_idea")

]
