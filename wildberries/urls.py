from django.urls import path

from wildberries.views import WildberriesView


urlpatterns = [
    path('products', WildberriesView.as_view(), name='products'),
]
