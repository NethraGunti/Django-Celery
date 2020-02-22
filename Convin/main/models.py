from django.db import models
from django.contrib.auth.models import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Task(models.Model):
    task_type=models.IntegerField(unique=True,blank=False, null=False)
    task_desc=models.TextField()
    # print('Hihug7yftdygcveduvfgjnefyb76gtru3f87gve3jubfhend')
    def update_task_desc():
        # print("\njrfviwfcnjdn\n\n\n\n\n\n")
        type=int(input('Enter the task you want to update'))
        desc=input("\nEnter the new task description or Enter 'none' for no changes")
        obj=Task.objects.get(task_type=type)
        if(desc!='none'):
            obj.task_desc=desc
            obj.save()
            print('\nChanges Made Successfully.\n')

        else:
            print('\nChanges Made Successfully.\n')

        return None

    def create_new_task():
        task=int(input("\nEnter the new task numeber"))
        desc=input("\nEnter the task description for the new task")
        new_task=Task(task_type=task,task_desc=desc)
        new_task.save()
        TaskTracker.create_new_tracker(task)
        return None

    def del_task():
        task=int(input("\nEnter the task type you want to delete: "))
        Task.objects.get(task_type=task).delete()




class TaskTracker(models.Model):
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    # task_type=models.IntegerField(blank=False, null=False)
    update_type=models.CharField(max_length=7)
    email=models.EmailField(_('email address'), unique=True)

    def create_new_tracker(task_type):
        if(task_type==None):
            task_type=int(input('Enter the task you want to create a new Tracker for: '))

        update=input('Enter the update type: ')
        id=input('Enter the email Id to be tracked: ')

        new_tracker=TaskTracker(task=Task.objects.get(task_type=task_type), update_type=update, email=id)
        new_tracker.save()

        return None
