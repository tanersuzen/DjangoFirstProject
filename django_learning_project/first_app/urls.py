from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #tanersuzen.com/first_app
    path("<int:number1>/", views.course_number_view, name="coursenumberview"), #tanersuzen.com/first_app/10 -> tanersuzen.com/first_app/kotlin
    path("<str:item>/", views.course, name="course"), #tanersuzen.com/first_app/python
    path("<int:num1>/<int:num2>/", views.multiply_view, name="multiply") #tanersuzen.com/first_app/5/4

    ]