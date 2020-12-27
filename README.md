Instala los requerimientos
```
pip3 install -r requirements.txt
```
Crear una DB en MySQL que se llame: appclima

Iniciar tablas desde Django
```
python manage.py makemigrations
python manage.py migrate
```

Crear superusuario
```
python manage.py createsuperuser
```
Checar que todo está bien
```
python manage.py check 
```

Iniciar servidor local
```
python manage.py runserver
```

recuerda agregar el archivo .env en el root del proyecto

SECRET_KEY=

DEBUG=True

DB_NAME=appclima

DB_USER=root

DB_PASSWORD=tu_contraseña

DB_HOST=localhost

API_KEY=