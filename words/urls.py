from django.urls import path

from . import views
"""
to jest kawałek pliku z mysite/urls.py:

urlpatterns = [
    path('words/', include('words.urls')), # tutaj do ścieżki words doklejane są ścieżki poniżej
    path('admin/', admin.site.urls),
]

czyli link to: http://127.0.0.1:8000/words/list-users

http://127.0.0.1:8000/ - adres strony, którą odpalać przez manage.py
words/ - podmontowanie w głównym pliku url wszystkich urli z poniższego pliku
list-users - ścieżka wskazująca na widok: views.ListUsers.as_view()

analogicznie inne funkcje, jak chcecie dodać nową zdefiniujcie tutaj ścieżkę i wskażcie na nową funkcję
z pliku views.py

"""

urlpatterns = [
    path('', views.index, name='index'),
    path('words', views.words, name='words'),
    path('czas', views.czas, name='czas'),
    path('list-users', views.ListUsers.as_view(), name='list-users'),
    path('test_get_post', views.test_get_post, name='test_get_post'),

]
