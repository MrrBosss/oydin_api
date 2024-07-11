from rest_framework.routers import DefaultRouter
from django.urls import path
from oydin.views import ProductViewSet



router = DefaultRouter()
urlpatterns = router.urls
urlpatterns += [
    path('products/', ProductViewSet.as_view(), name='products')
]