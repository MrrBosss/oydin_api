from rest_framework.routers import DefaultRouter
from django.urls import path

from oydin.views import ProductViewSet, BrandViewSet, ProductShotsViewSet, CategoryViewSet, ProductListView



router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('brands', BrandViewSet, basename='brands')
router.register('categories', CategoryViewSet, basename='categories')
router.register('product-shots', ProductShotsViewSet, basename='product-shots')
urlpatterns = router.urls
urlpatterns += [
    path('product-list', ProductListView.as_view(), name='product-list')
]