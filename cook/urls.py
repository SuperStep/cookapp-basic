from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.recipies_list, name = 'recipies_list'),
    path('recipie/<int:pk>', views.recipie_detail, name = 'recipie_detail'),
    path('recipie/<int:pk>/delete/<int:ingredient_pk>', views.recipie_detail_delete, name='recipie_detail_delete'),
    #path('recipie/<int:pk>/edit/', views.post_edit, name='recipie_edit'),    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

