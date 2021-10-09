from django.urls import path
from . import views
from articles.class_views import (
IndexView, ArticleDetailView
)


urlpatterns = [
    path('article/', IndexView.as_view(), name='article'),
    # path("article/", views.article, name="article"),
    # path("articledetail/<int:article_id>", views.article_detail, name="article_detail"),
    path('<slug:slug>', ArticleDetailView.as_view(), name="detail"),
    path("addarticle/", views.add_article, name="add_article"),
    path("savearticle/", views.save_article, name="save_article"),
    path("editarticle/<int:article_id>", views.edit_article, name="edit_article"),
    path("saveeditarticle/<int:article_id>", views.save_edit_article, name="save_edit_article"),
    path("deletearticle/<int:article_id>", views.delete_article, name="delete_article")
]
