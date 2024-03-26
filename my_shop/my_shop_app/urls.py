from django.urls import path
from .views import home,catalog,contacts,about_us,log_page,order_product,about_product

urlpatterns = [
    path('home/', home, name='home'),
    path('catalog/<str:category>/', catalog, name='catalog/<str:category>/'),
    path('contacts/', contacts, name='contacts'),
    path('about_us/', about_us, name='about_us'),
    path('log_page/', log_page, name='log_page'),
    path('order/', order_product, name='order_product'),
    path('product/<int:product_id>/', about_product, name='product_detail')

]