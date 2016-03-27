### This is deploy manual for attract app (test_task).



**1. git clone https://github.com/Andrewdiss/AttractGroup.git**

**2. cd AttractGroup**

**3. virtualenv env**

**4. .env/bin/activate**

**5. pip install -r req.txt**

**6. ./manage.py migrate**

**7. ./manage.py runserver**

by default server should start at http://127.0.0.1:8000

**8. open url in browser window and switch to admin panel** 

http://127.0.0.1:8000/admin/ 
* login - admin
* password - password3

in "education/people" field you can find people list and their related education

**4. ctrl+c**  stop server through terminal

**5. ./manage.py**

in [education] field check following script commands:

* edu_check
* gmail
* weather

**6. python manage.py weather -h**

to see help information and positional arguments 

**7. python manage.py gmail login password**

mail check may fail if your gmail account block unsafe connections

remove restriction folowing [this](https://support.google.com/accounts/answer/6010255) instructions
