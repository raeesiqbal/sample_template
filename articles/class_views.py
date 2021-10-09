from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from articles.models import Article, Subject
from users.models import User
from django.views.generic import ListView, View, TemplateView, DetailView


class IndexView(ListView):
    model = Article
    template_name = 'articles/class_articles.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/class_articledetail.html'
    context_object_name = 'article'
