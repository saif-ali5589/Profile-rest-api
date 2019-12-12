from django.urls import path

from profile_app import views


#as_view functon is invild funtion for api view
urlpatterns = [
                path('hello-view/',views.HelloApiViews.as_view()),
            ]
