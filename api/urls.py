from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('home/', views.allproducts),
    path('postproduct/',views.post_product),
    path('editproduct/<int:id>/', views.Edit_product),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)