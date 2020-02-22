from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *
import time
from .models import Task, TaskTracker


def track(request):
    print('Please Load the webpage and come back here. Open a new terminal and run the commane "celery -A Convin worker -B --loglevel=info"')

    while(True):
        print('\n-------------------\nStarting Again\n-------------------\n')
        time.sleep(3)
        print('\n\n----------------------------\nExisting Tasks and Trackers\n----------------------------')

        if TaskTracker.objects.first():
            for obj in TaskTracker.objects.all():
                print('\nTask Type:\t' + str(obj.task.task_type) + '\nTask Description:\t' + obj.task.task_desc + '\nUpdate Type:\t' + obj.update_type + '\nEmail:\t' + obj.email)
        else:
            print('None\n')
        choice=int(input('\n----------------------------\nEnter to choose:\n1. Create New Task\n2. Update Existing Task Description\n3.Create New Task Tracker\n4.Delete Tracker\n5.Exit\n----------------------------\n'))

        if(choice==5):
            break

        else:
            if choice==1:
                try:
                    task=int(input("\nEnter the new task numeber"))
                except (ValueError,TypeError):
                    print('\nMust be an Integer and non-empty. Try Again!')
                    return False

                stat1=Task.create_new_task(task)
                if (not stat1) and (Task.objects.filter(task_type=task).exists()):
                    Task.objects.get(task_type=task).delete()


            elif choice==2:
                Task.update_task_desc(type)



            elif choice==3:
                TaskTracker.create_new_tracker(task_type=None)
            elif choice==4:
                Task.del_task()
            else:
                print('Invalid Choice'),
    return HttpResponse('You can always refresh the page and start again!')
