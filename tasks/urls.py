# se crea este archivo para definir las rutas de la app tasks

from django.urls import path                     # importo la función path para definir rutas
from .views import TaskListView                  # importo la vista basada en clase que muestra la lista de tareas


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks_list'),    # es una lista de funciones, el primer argumento es la ruta, el segundo es la vista que se ejecuta, y el tercero es el nombre de la ruta
]                                                           # la ruta '' es la ruta raíz de la app, que en este caso es /tasks