# Arata

## Requisitos

- Python 3.11.6

## Instalación

1. Clona este repositorio:

```bash
   git clone https://github.com/Aldana2005/Arata.git
```

2. Ve al directorio del proyecto:

```bash
   cd Arata
```

3. Crea un entorno virtual (se recomienda usar virtualenv):

  ```bash
     python -m venv venv
```
  
4. Activa el entorno virtual:

  - En Windows:

   ```bash
       cd venv\Scripts
   ```
   ```bash
      activate
   ```
    
  - En Unix o MacOS:

```bash
   source venv/bin/activate
```

5. Instala las dependencias:

```bash
   pip install -r requirements.txt
```

6. Aplica las migraciones:

```bash
   python manage.py makemigrations
```
```bash
   python manage.py migrate
```

7. Uso
    - Ejecuta el servidor de desarrollo:

```bash
   python manage.py runserver
```
El proyecto estará disponible en http://localhost:8000/.

8. Contribuciones
  Si deseas contribuir, sigue estos pasos:

- Haz un fork del repositorio.
- Crea una rama para tu función: `git checkout -b feature/nueva-funcion.`
- Realiza tus cambios y haz commit: `git commit -m 'Añade nueva función'`.
- Haz push a la rama: `git push origin feature/nueva-funcion`.
- Abre un pull request en GitHub.

