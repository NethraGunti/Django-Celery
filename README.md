# ConvinRepo

Please follow the instructions:

1. Clone the repository into a directory

2. Install the virtualenv requirements
        'cd ../ConvinRepo'
        "using pip3 install -r requirements.txt"
        Also make sure to run 'sudo apt-get install rabbitmq-server'
        
3. Open another terminal in the location 'ConvinRepo/Convin'

5. In one terminal run the command "celery -A Convin worker -B --loglevel=info"

4. In another terminal run the django-server using "python3 manage.py runserver"

6. Now visit the link(localhost address) shown in the django-server terminal.

7. Go back to the terminal and you are good to go.

8. In case of any errors, refresh the webpage and you'll be fine.

9. In the first terminal, you can see the task alerts being sent as scheduled

10. You can change the schedule time by going into settings.py
