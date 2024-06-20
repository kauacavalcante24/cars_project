from django.contrib import admin
from django.urls import path
from django.conf import settings #configurações para imagens
from django.conf.urls.static import static #configuração para imagens
from cars.views import CarListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from account.views import create_account, login_view, logout_view


urlpatterns = [
    #     Rota           #View
    path('admin/', admin.site.urls),
    path('account/', create_account, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('cars/', CarListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_cars_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'), #pk = primary key
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #configuração para imagens
