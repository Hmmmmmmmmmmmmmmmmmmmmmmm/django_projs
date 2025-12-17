from django.urls import path
from . import views

# urlpatterns = [
#     path("",views.main_func),
#     path("january", views.index)
# ]
urlpatterns = [
    path('', views.main_func, name='main'),
    # path('january/', views.january, name='january'),
    # path('february/', views.february, name='february'),
    # path('march/', views.march, name='march'),
    # path('april/', views.april, name='april'),
    # path('may/', views.may, name='may'),
    # path('june/', views.june, name='june'),
    # path('july/', views.july, name='july'),
    # path('august/', views.august, name='august'),
    # path('september/', views.september, name='september'),
    # path('october/', views.october, name='october'),
    # path('november/', views.november, name='november'),
    # path('december/', views.december, name='december'),
    path('<int:month>',views.monthly_view_number_based,name='number_based_month'),
    path('<str:month>',views.month_view,name='month'),
   ]