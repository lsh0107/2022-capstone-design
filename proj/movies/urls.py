from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item_based', views.item_based, name='item_based'),
    path('matrix_factorization', views.matrix_factorization, name='matrix_factorization')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
