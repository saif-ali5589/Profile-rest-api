from django.urls import path , include
from rest_framework.routers import DefaultRouter
from profile_app import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)
#we dont need to specify the base name because we already define queryset which automatically take base call

#as_view functon is invild funtion for api view
urlpatterns = [
                path('hello-view/',views.HelloApiViews.as_view()),
                path('',include(router.urls)),
            ]
