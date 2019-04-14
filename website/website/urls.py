from django.conf.urls import url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^home/', views.index),
    url(r'^python/', views.python),
    url(r'^django/', views.django),
    url(r'^mysql/', views.index),
    url(r'^copyright/', views.copyright),
    url(r'^contact/', views.contact)

]
