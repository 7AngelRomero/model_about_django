from django.shortcuts import render
from .models import Task                    # importo el modelo Task  
from django.views.generic import ListView   # me permite crear vistas basadas en clases

# Create your views here.

class TaskListView(ListView):               # heredo de ListView para mostrar una lista de objetos
    model = Task                            # especifico el modelo a usar
    template_name = 'tasks_list.html'  # especifica la plantilla a usar


