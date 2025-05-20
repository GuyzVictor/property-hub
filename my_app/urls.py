from django.urls import path
from .views import *

app_name = "my_app"

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contact-us/", contact, name="contact_us"),
    path("services/", services, name="services"),
    path("properties/", properties, name="properties"),
    path("property-details/", property_details, name="property_details")
]
