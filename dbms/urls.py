from django.urls import path

from dbms import views as v

urlpatterns = [
    path("", v.index, name="index"),
    path("index_naver/", v.index_naver, name="index_naver"),
    path("list/", v.list, name="list")
]
