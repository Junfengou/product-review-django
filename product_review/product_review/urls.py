
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from review_stuff import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.product_list),
    path('products/', views.product_list),
    url(r'^api/products/$', views.product_list),
    url(r'^api/products/(?P<pk>[0-9]+)$', views.getProduct),

    path('reviews/', views.review_list),
    url(r'^api/reviews/$', views.review_list),
    url(r'^api/reviews/(?P<pk>[0-9]+)$', views.getReview),

    path('profiles/', views.profile_list),
    url(r'^api/profiles/$', views.profile_list),
    url(r'^api/profiles/(?P<pk>[0-9]+)$', views.getProfile),
]
