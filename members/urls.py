from django.urls import path
from . import views
from .views import products_view, index_view, car1_view, car6_view, car5_view, car4_view, car3_view, car2_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('members/', views.members, name='members'),
    path('products/', products_view, name='products'),
    path('car1/', car1_view, name='car1'),
    path('car2/', car2_view, name='car2'),
    path('car3/', car3_view, name='car3'),
    path('car4/', car4_view, name='car4'),
    path('car5/', car5_view, name='car5'),
    path('car6/', car6_view, name='car6'),
    path('', index_view, name='index'),  # Home page redirects to index.html
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)