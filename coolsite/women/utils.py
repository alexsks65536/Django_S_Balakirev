from women.models import *

"""
Главное меню
"""
menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Проверка стилей', 'url_name': 'css_example'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()  # делаем копию меню.
        if not self.request.user.is_authenticated:  # если user не авторизован, убираем пункт меню "Добавить статью"
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:  # Переопределить ключ cat_selected = 0, если его нет в **kwargs
            context['cat_selected'] = 0
        return context
