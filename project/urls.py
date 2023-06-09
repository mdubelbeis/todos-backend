from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todos import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet, "users")
router.register(r"todos", views.TodoViewSet, "todos")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
