from django.urls import path
from . import views


urlpatterns = [
    path("news/", views.news, name="news"),
    path("newsdetail/<int:news_id>", views.news_detail, name="news_detail"),
    path("addnews/", views.add_news, name="add_news"),
    path("savenews/", views.save_news, name="save_news"),
    path("editnews/<int:news_id>", views.edit_news, name="edit_news"),
    path("saveeditnews/<int:news_id>", views.save_edit_news, name="save_edit_news"),
    path("deletenews/<int:news_id>", views.delete_news, name="delete_news"),
    path("addnewsvideo/<int:news_id>", views.add_news_video, name="add_news_video"),
    path("savenewsvideo/<int:news_id>", views.save_news_video, name="save_news_video"),
    path("deletenewsvideo/<int:news_id>/<int:video_id>", views.delete_news_video, name="delete_news_video"),
]
