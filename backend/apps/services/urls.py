from django.urls import path
from apps.services import views

app_name = 'services'

urlpatterns= [
    path('', views.ListServices.as_view(), name='services'),
    path('<pk>', views.ServiceDetailView.as_view(), name='services'),
    path('service_types/', views.ListServiceTypes.as_view(), name='service_types'),
    # path('teams/', views.ListServiceTypes.as_view(), name='service_teams'),
    # path('teams/<pk>', views.TeamDetailView.as_view(), name='service_team'),
    path('order/', views.ListOrderItems.as_view(), name='service_orders'),
    path('order/<pk>', views.ServiceOrderItemDetailView.as_view(), name='service_order'),
]