from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .models import Task, TaskCategory


def TasksAll(request):
    all_tasks = Task.objects.all()
    ordered_tasks = Task.objects.filter(
        task_done="False").order_by('-created_date')
    all_categories = TaskCategory.objects.all()
    context = {'tasks': all_tasks, 'ordered_tasks': ordered_tasks, 'categories': all_categories}
    return render(request, 'todoapp/todos.html', context)


def TaskDone(request, num):
    queryset = Task.objects.filter(pk=num).update(task_done="True")
    return redirect('task_all')
    

class TaskByCategoryViewList(generic.ListView):
    model = Task
    context_object_name = 'task_by_category'
    template_name = 'todoapp/task_by_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(TaskCategory, category_name=self.kwargs['category'])
        print(self.category)
        return Task.objects.filter(category__category_name=self.category)


class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'todoapp/task_detail_list.html'


class TaskAdd(generic.CreateView):
    model = Task
    fields = ('name', 'category', 'description', 'task_date', 'task_important')
    template_name_suffix = '_add_form'
    success_url = reverse_lazy('task_all')


class TaskUpdate(generic.UpdateView):
    model = Task
    fields = ('name', 'category', 'description', 'task_date', 'task_important')
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('task_all')


class TaskDelete(generic.DeleteView):
    model = Task
    template_name_suffix = '_delete_confirm'
    success_url = reverse_lazy('task_all')
