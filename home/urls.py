from django.urls import path
from .views import IndexView, TermsOfServiceView

urlpatterns = [
    path("", IndexView, name="home"),
    path("tos/",TermsOfServiceView.as_view(), name="tos")
]
