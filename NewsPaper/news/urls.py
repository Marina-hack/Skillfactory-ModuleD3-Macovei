from django.urls import path
# Импортируем созданное нами представление
from .views import BreakingNews, News, Articles
from . import views

urlpatterns = [
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
    path('news', News.as_view()),
    # path('news/<int:pk>', News.as_view()),
    path('news/<int:pk>', BreakingNews.as_view()),
    path('articles/<int:pk>', Articles.as_view()),
  ]
# pk — это первичный ключ товара, который будет выводиться у нас в шаблон
# int — указывает на то, что принимаются только целочисленные значения

