

from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('form/', views.data, name='form'),
    # path('form/', views.DataCreateView, name='form'),
    # path('dataform/', views.add_data, name='dataform'),
    # path('add/', views.DataListView.as_view(), name='add'),
    path('ajax/load-branch/', views.load_branch, name='ajax_load_branch'),
    # path('<slug:c_slug>/', views.add_branch, name='products_by_category'),

]

