from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^article/(\d+)/', views.viewArticle, name = 'article'),
]
