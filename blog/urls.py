from django.urls import path
from .views import PostListView, PostDetailView, EmailPostView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('form/', EmailPostView.as_view(), name='form'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', PostDetailView.as_view(), name='post_detail')
]
