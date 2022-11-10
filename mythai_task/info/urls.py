from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('api/auth/', include('djoser.urls')),
    path('admin/', admin.site.urls, name='admin'),

    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),

    path('todo/<str:username>', views.todo, name='todo'),
    path('delete/<int:todo_id>/<str:username>', views.delete, name='delete'),
    path('update/<int:todo_id>/<str:username>', views.update, name='update'),
    path('add/<str:username>', views.add, name='add'),

    path('photos/<str:username>', views.photos, name='photos'),
    path('photo_add/<str:username>', views.photo_add, name='photo_add'),
    path('photo_delete/<int:photo_id>/<str:username>', views.photo_delete, name='photo_delete'),
]
admin.site.site_url = None
admin.site.site_header = 'ADMİN LOGİN'
