from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', WomenAbout.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('css_example/', CssExample.as_view(), name='css_example'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]


