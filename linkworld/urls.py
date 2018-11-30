from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", views.UserView)
router.register("posts", views.PostView)
router.register("comments", views.CommentView)


urlpatterns = [
   path("", include(router.urls)),

]