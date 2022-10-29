from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *

"""
Главное меню
"""
menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'  # указываем путь к шаблону
    context_object_name = 'posts'  # переменная контекста

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передача динамического контекста
        """
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        """
        Выбор постов, которые помечены для публикации
        """
        return Women.objects.filter(is_published=True)


# def index(request):  # HttpRequest
#     posts = Women.objects.all()  # Подключаемся к БД Women, считываем все значения и передаем в шаблон переменные
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#     }
#     return render(request, 'women/index.html', context=context)


def about(request):  # HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')  # Адрес маршрута перенаправления после добавления поста

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передача динамического контекста
        """
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context


# def addpage(request):
#     """
#     Форма добавления статьи на сайт
#     """
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#         print(form.cleaned_data)
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_slug):
#     """
#     Функция отображения поста, выбирает по slug-ам
#     """
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context=context)

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Передача динамического контекста
        """
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # генерация ошибки 404, если адрес недействителен

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_slug):
#     """
#     Функция отображения постов по категориям, выбирает по slug-ам
#     """
#     cat = Category.objects.get(slug=cat_slug)
#     posts = Women.objects.filter(cat_id=cat.id)
#
#     if len(posts) == 0:  # если нет такой категории, генерирует "Страница на найдена"
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_slug,
#     }
#     return render(request, 'women/index.html', context=context)
