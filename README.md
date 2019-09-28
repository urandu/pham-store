## Pharm-store API
This is the backend for pharm-store

### Installation
 - Have docker installed 
 - clone this repository `git clone https://github.com/urandu/pham-store.git`
 - `cd pharm-store`
 - `docker-compose up`
 - `docker-compose run api python manage.py createsuperuser`
 - `docker-compose run api python manage.py makemigrations`
 - `docker-compose run api python manage.py migrate`

### API swagger documentation

- Swagger API doc located at http://localhost:8900/swagger