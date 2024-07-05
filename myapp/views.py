

# Create your views here.


from django.shortcuts import render, redirect
from .forms import UserForm, TaskForm

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user.html', {'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})




from django.http import HttpResponse
from openpyxl import Workbook

def export_to_excel(request):
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "Users"
    ws1.append(["ID", "Name", "Email", "Mobile"])
    for user in User.objects.all():
        ws1.append([user.id, user.name, user.email, user.mobile])

    ws2 = wb.create_sheet(title="Tasks")
    ws2.append(["ID", "Task Details", "Task Type", "User"])
    for task in Task.objects.all():
        ws2.append([task.id, task.task_details, task.task_type, task.user.name])

    response = HttpResponse(content=wb, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=users_and_tasks.xlsx'
    wb.save(response)
    return response
