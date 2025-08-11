from rest_framework.routers import DefaultRouter
from django.urls import path

from oydin.views import BrandViewSet, ProductShotsViewSet, CategoryViewSet, ProductListView, \
    ProductDetailView, CharacteristicViewSet, OrderView, NewsViewSet



router = DefaultRouter()
router.register('characteristics', CharacteristicViewSet, basename='characteristics')
router.register('brands', BrandViewSet, basename='brands')
router.register('categories', CategoryViewSet, basename='categories')
router.register('news', NewsViewSet, basename='news')
router.register('product-shots', ProductShotsViewSet, basename='product-shots')
urlpatterns = router.urls
urlpatterns += [
    path('orders/', OrderView.as_view(), name='orders'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-retrieve')
]