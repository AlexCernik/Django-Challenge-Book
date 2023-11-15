# Django Challenge Book

</br>
- <b>Instalar las dependencias.</b>

```
pip install -r requirements.txt
```
</br>
- <b>Hacer las migraciones.</b>

```
python manage.py makemigrations
python manage.py migrate
```
</br>
- <b>Crear un super usuario.</b>

```
python manage.py createsuperuser
```
</br>
- <b>Iniciar el servidor.</b>

```
python manage.py runserver
```
</br>

# Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| /api/auth/ | POST | Iniciar sesión |
| /api/auth/signin/ | POST | Registrarse |
| /api/book/ | GET | Listar todos los libros creados por el usuario |
| /api/book/:id/ | GET | Obtener detalles de un libro en específico |
| /api/book/ | POST | Crear un nuevo libro |
| /api/book/:id/ | PUT | Actualizar los detalles del libro |
| /api/book/:id/ | DELETE | Eliminar un libro por el ID |