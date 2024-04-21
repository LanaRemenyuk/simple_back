## Project: simple_back 
### Decription: 
##### Simple website (admin dashboard, customer and provider accounts)

### Technologies:

- Python 3.11.0
- Django==5.0.4
- djangorestframework==3.15.1
- djangorestframework-simplejwt==5.3.1
- psycopg2==2.9.9
- drf-yasg==1.21.7

### How to launch locally:

Clone the repository and move there through the command line:
```sh
git clone https://github.com/LanaRemenyuk/simple_back -> cd your_file_location/simple_back
```
Install the virtual environment, activate it and install dependencies:
```sh
install poetry if needed -> poetry shell && poetry install 
```
Apply migrations:
```sh
python manage.py migrate
```
Create a superuser:
```sh
python manage.py createsuperuser
```
Start the local server:
```sh
python manage.py runserver
```


- documentation: http://127.0.0.1:8000/redoc/ | http://127.0.0.1:8000/swagger/

- admin: http://127.0.0.1:8000/admin/ 

- account app routes
```
GET get main page: http://127.0.0.1:8000

```
```
GET get main page: http://127.0.0.1:8000

```
```
GET get my account as a customer: http://127.0.0.1:8000/customer/

```
```
POST add data to a customer profile: http://127.0.0.1:8000/customer/update

```
```
GET get my account as a provider: http://127.0.0.1:8000/provider/

```

```
POST add data to a provider profile: http://127.0.0.1:8000/provider/update

```

extra functionality (auth): 

- jwt routes 
```
POST get bearer tokens: http://127.0.0.1:8000/auth/jwt/create/

{"email":"e2828@yandex.ru",
"password":"cut12cut123"}
```
```
POST get bearer tokens: http://127.0.0.1:8000/auth/jwt/refresh/

{"refresh":"ur_refresh_token_here"}
```
- user routes
```
POST sign up: http://127.0.0.1:8000/auth/auth/

{"email":"user@yandex.ru",
"password":"userpass123",
"first_name":"user",
"last_name":"jackson"}
```
```
GET get user (authorized with bearer): http://127.0.0.1:8000/auth/auth/{user_id}/ 

```
```
GET get userlist (admin only): http://127.0.0.1:8000/auth/auth/

```
```
PUT edit user (authorized with bearer): http://127.0.0.1:8000/auth/auth/{user_id}/ 

{"email":"user@yandex.ru",
"password":"userpass126",
"first_name":"user",
"last_name":"jackson"}
```

```
DELETE delete user (authorized with bearer): http://127.0.0.1:8000/auth/auth/{user_id}/ 
```
