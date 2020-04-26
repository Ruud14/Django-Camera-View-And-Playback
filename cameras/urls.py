from django.urls import path
from . import views

urlpatterns = [
    path('<cam_name>', views.watch, name='cam_name'),
    path('<cam_name>/replay/',views.replay, name='page_number'),
    path('<cam_name>/replay/<page_number>',views.replay, name='page_number'),
]