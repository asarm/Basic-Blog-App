from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="home"),
    path('<int:post_id>/post/',views.detail,name="detail_page"),
]
