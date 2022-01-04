from django.urls import path

from api.views import *

urlpatterns = [
	path('search/', ProductModelListAPIView.as_view()),
	path('category/<int:pk>/', ProductModelListAPIView.as_view()),
	path('order/<int:pk>/', OrderListAPIView.as_view()),
	path('order/', OrderModelCreateAPIView.as_view()),
	path('user/<int:pk>/', UserModelListAPIView.as_view()),
	path('products/<int:pk>/', ProductModelRetrieveAPIView.as_view()),

	path('users/register/', UserModelCreateAPIView.as_view()),
	path('category/', CategoryModelListAPIView.as_view()),
]
