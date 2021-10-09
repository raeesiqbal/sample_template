from django.urls import path
from . import views


urlpatterns = [
    path("thread/", views.thread, name="thread"),
    path("threaddetail/<int:thread_id>", views.thread_detail, name="thread_detail"),
    path("addthread/", views.add_thread, name="add_thread"),
    path("savethread/", views.save_thread, name="save_thread"),
    path("editthread/<int:thread_id>", views.edit_thread, name="edit_thread"),
    path("saveeditthread/<int:thread_id>", views.save_edit_thread, name="save_edit_thread"),
    path("deletethread/<int:thread_id>", views.delete_thread, name="delete_thread")
]
