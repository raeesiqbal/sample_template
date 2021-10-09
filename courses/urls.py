from django.urls import path
from . import views


urlpatterns = [
    path("courses/", views.course, name="course"),
    path("coursedetail/<int:course_id>", views.course_detail, name="course_detail"),
    path("addcourse/", views.add_course, name="add_course"),
    path("savecourse/", views.save_course, name="save_course"),
    path("editcourse/<int:course_id>", views.edit_course, name="edit_course"),
    path("saveeditcourse/<int:course_id>", views.save_edit_course, name="save_edit_course"),
    path("deletecourse/<int:course_id>", views.delete_course, name="delete_course"),
    path("minidetails/<int:course_id>", views.mini_details, name="mini_details"),
    path("addvideo/<int:course_id>", views.add_video, name="add_video"),
    path("savevideo/<int:course_id>", views.save_video, name="save_video"),
    path("deletevideo/<int:video_id>/<int:course_id>", views.delete_video, name="delete_video")

]
