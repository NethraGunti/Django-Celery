from django.db import models
from django.contrib.auth.models import models
from django.utils.translation import ugettext_lazy as _
from django.db import IntegrityError
# Create your models here.

class Task(models.Model):

    task_type=models.IntegerField(unique=True,blank=False, null=False)
    task_desc=models.TextField(blank=False, null=False)


    def create_new_task(task):

        try: #input task desc with error handling
            desc=input("\nEnter the task description for the new task: ")
            if not desc:
                raise ValueError('Empty Description')
        except ValueError as e:
            print('\nString must be non-empty\n')
            return False
        except TypeError:
            print('\nMust be a String\n')
            return False


        try: #making Task object with error handling
            new_task=Task(task_type=task,task_desc=desc)
            new_task.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                print('\nTask Type already exists. Try Again!\n')
                return False

        if not TaskTracker.create_new_tracker(task):
            # new_task.delete()
            print('\nCouldn\'t create new task. Try Again!\n')
            return False
        else:
            print('\nNew Task and Tracker created Successfully\n')
            return True



    def update_task_desc(type):

        try:
            type=int(input('Enter the task type you want to update: '))
        except (ValueError,TypeError):
            print('\nMust be an Integer and non-empty. Try Again!\n')
            return None

        try:
            desc=input("\nEnter the new task description or Enter 'none' for no changes: ")
            if not desc:
                raise ValueError('Empty Description')
        except ValueError as e:
            print('\nString must be non-empty\n')
            return None
        except TypeError:
            print('\nMust be a String\n')
            return None



        obj=Task.objects.get(task_type=type)
        if(desc!='none'):
            obj.task_desc=desc
            obj.save()
            print('\nChanges Made Successfully.\n')

        else:
            print('\nNo Changes Made.\n')

        return None





    def del_task():

        try:
            task=int(input('Enter the task type you want to Delete'))
        except (ValueError,TypeError):
            print('\nMust be an Integer and non-empty. Try Again!')
            return False

        if Task.objects.filter(task_type=task).exists():
            Task.objects.get(task_type=task).delete()
            print('\nTask Deleted Successfully\n')
            return True
        else:
            print('\nNo such task exists.\n')
            return False



class TaskTracker(models.Model):

    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    update_type=models.CharField(max_length=7)
    email=models.EmailField(_('email address'), unique=True)

    def create_new_tracker(task_type):
        if(task_type==None):
            task_type=int(input('Enter the task you want to create a new Tracker for: '))

        if not Task.objects.filter(task_type=task_type).exists():
            print('\nNo such task exists\n')
            return False

        else:
            try:
                update=input('Enter the update type (daily/weekly/monthly): ')
                if not update:
                    raise ValueError('\nEmpty String\n')
            except ValueError as e:
                print('\nString must be non-empty\n')
                return False
            except TypeError:
                print('\nMust be a String\n')
                return False

            try:
                id=input('Enter the email Id to be tracked: ')
                if not id:
                    raise ValueError('Empty Email Id')
            except ValueError as e:
                print('\nString must be non-empty\n')
                return False
            except TypeError:
                print('\nMust be an email\n')
                return False

            try:
                new_tracker=TaskTracker(task=Task.objects.get(task_type=task_type), update_type=update, email=id)
                new_tracker.save()
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    print('Email Already Exists.')
                    return False
            except (ValueError,TypeError):
                print('Something\'s Wrong. Make sure to have gotten all the fields correctly. Try Again!')
                return False

            print('\nTracker created successfully.\n')
            return True
