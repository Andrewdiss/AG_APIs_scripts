### This is deploy manual for attract app (test_task).
####Follow the instructions below


**1) git clone https://github.com/Andrewdiss/AttractGroup.git**

**2) cd AttractGroup**

**3) virtualenv env**

Create virtual environment "env" in directory

**4) . env/bin/activate**

**5) pip install -r req.txt**

**6) cd attract**

**7) python manage.py runserver**

by default server should start at http://127.0.0.1:8000

**8) open url in browser window and switch to admin panel** 

http://127.0.0.1:8000/admin/ 
* login - admin
* password - password3

in "education/people" field you can find people list and their related education

**9) ctrl+c**  stop server through terminal

**10) python manage.py**

in [education] field check following script commands:

* edu_check
* gmail
* weather

**11) python manage.py script -h**

to see help information and positional arguments 

**12) python manage.py edu_check all**

lists all persons with no filter

**13) python manage.py edu_check master**

lists persons with master degree

**14) python manage.py weather Odessa**

return city name, country, temperature, wind speed etc.

**15) python manage.py gmail login password**

mail check may fail if your gmail account block unsafe connections

remove restriction folowing [this](https://support.google.com/accounts/answer/6010255) instructions

return last email information: subject, from, to, date  
