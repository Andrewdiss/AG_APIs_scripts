### This is deploy manual for attract app (test_task).

it`s recomended to use new virtualenv folder to deploy this project 
After "git clone url" you should use commands in following order

**1. pip install -r req.txt**

**2. python manage.py runserver**

use command within app fodler
by default server should start at http://127.0.0.1:8000

**3. open url in browser window and switch to admin panel** 

http://127.0.0.1:8000/admin/ 
* login - admin
* password - password3

in "education/people" field you can find people list and their related education

**4. ctrl+c**  stop server through terminal

**5. python manage.py**

in [education] field you can see following script commands:

* edu_check
* gmail
* weather

**6. python manage.py weather -h**

to see help information and positional arguments 

