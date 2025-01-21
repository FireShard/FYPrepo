from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'UserLaptop', views.UserLaptopViewSet)
router.register(r'LaptopDetails', views.LaptopDetailsViewSet)

urlpatterns = [
<<<<<<< HEAD
    path('', include(router.urls)),
=======
    path('', include(router.urls))
>>>>>>> 747fc1f3b5d1ae841d7631ca7dba34fc42cbe430
]
