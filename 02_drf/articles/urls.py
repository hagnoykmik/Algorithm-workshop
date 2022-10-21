from django.urls import path
from . import views


urlpatterns = [
    # get으로 요청이 들어오면 전체 게시글 목록을 담은 json을 준다
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
