from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('emprestimos', views.AprovadoView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
	path('emprestimos/criar', views.cxcontact, name='cxform'),
    path('emprestimo/<int:id>/ver', views.detalhes, name='detalhes'),
    path('emprestimo/<int:id>/editar', views.editar, name='editar'),
] 