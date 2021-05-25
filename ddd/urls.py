from api.views import GraphQLView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('graphql', GraphQLView.as_view()),
    path('admin/', admin.site.urls),
]
