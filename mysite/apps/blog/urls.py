from django.urls import path

from . import views


urlpatterns = [
	path('posts/', views.index, name="index"),
	path('posts/create', views.create_post, name="create-post"),
	path('posts/<int:id>', views.detail_post, name="detail-post"),
	path('posts/<int:id>/delete', views.delete_post, name="delete-post"),
	path('posts/<int:id>/update', views.update_post, name="update-post"),
]