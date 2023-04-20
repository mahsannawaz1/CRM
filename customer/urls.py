from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('add/', views.addProduct, name='add_product'),
    path('list/', views.listProducts, name='list_products'),
    path('update/<int:pk>', views.updateProduct, name='update_product'),
    path('delete/<int:pk>', views.deleteProduct, name='delete_product'),
    path('create_order', views.OrderCreateView.as_view(
        template_name='customer/create_order.html'), name='create_order'),
    path('<int:pk>/update', views.OrderUpdateView.as_view(
        template_name='customer/update_order.html'), name='update_order'),
    path('<int:pk>/delete', views.OrderDeleteView.as_view(
        template_name='customer/delete_order.html'), name='delete_order'),
    path('order_list', views.ListOrdersView.as_view(
        template_name='customer/order_list.html'), name='list_orders'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
