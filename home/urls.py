from django.urls import path
from .views import IndexView, TermsOfServiceCreate

urlpatterns = [
    path("", IndexView, name="home"),
    path("tos/create/", TermsOfServiceCreate.as_view(), name="tos-create")
]
