from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .feeds import LatestPostsFeed
from .sitemaps import PostSitemap
from . import views

app_name = 'blog'

sitemaps = {
'posts': PostSitemap,
}

urlpatterns = [
    # post views

    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search')

]