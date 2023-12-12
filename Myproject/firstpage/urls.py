from django.urls import path
from . import views

urlpatterns = {
    path("",views.index),
    # path("<int:number>",views.firstpage_by_number),
    path("<str:mon>",views.firstpage)
}

