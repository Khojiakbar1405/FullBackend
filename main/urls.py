from django.urls import path
from .views import about, contact, main, service

urlpatterns = [
    path('about/', about),
    path('contact/', contact),
    path('', main),
    path('service/', service),
]

# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', main),
#     path('single', contact)
# ]
# # urls.py
