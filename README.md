
# **Django CRUD Animes**

## Descripció

Aquesta aplicació web permet gestionar animes i personatges, amb un **CRUD complet** (Crear, Llegir, Actualitzar, Eliminar). S'utilitza el **framework Django** per crear l'aplicació, amb una base de dades SQLite i una relació entre els animes i els seus personatges.

![Anime app example](/img/anime.png) 

## Funcionalitats

- Creació d'animes amb títol, autor i any.
- Creació de personatges vinculats a un anime.
- CRUD complet per a animes i personatges.
- Administrador per gestionar animes i personatges.

## Requisits

- Python 3.x
- Django 3.x

## Com començar

### 1. Clona aquest repositori:

```bash
git clone https://github.com/joysantalola/Framework-Django.git
````

### 2. Crea i activa un entorn virtual:

```bash
python3 -m venv env
source env/bin/activate   # Per Linux/Mac
env\Scripts\activate      # Per Windows
```

### 3. Instal·la les dependències:

```bash
pip install -r requirements.txt
```

### 4. Fes les migracions:

```bash
python manage.py migrate
```

### 5. Crea un superusuari:

```bash
python manage.py createsuperuser
```

### 6. Inicia el servidor:

```bash
python manage.py runserver
```

### 7. Accedeix a la web:

```url
http://127.0.0.1:8000/
```

### 8. Com accedir a l'admin:

1. Ves a `http://127.0.0.1:8000/admin/`.

   ![Admin Panel Example](URL_DE_LA_TUYA_CAPTURA_ADMIN)  <!-- Afegir captura de l'admin -->

2. Fes login amb el superusuari creat.

### 9. Afegir Anime i Personatge:

Captura del formulari per afegir un anime i els personatges dins de l'admin.

![Afegir Anime i Personatge](URL_DE_LA_TUYA_CAPTURA_FORMULARI)  <!-- Afegir captura dels formularis d'afegir Anime i Personatge -->

## Imatges

### Exemple de llista d'animes amb personatges vinculats:

![Exemple llista Anime amb Personatges](URL_DE_LA_TUYA_CAPTURA_LLISTA_ANIMES)  <!-- Afegir captura de la llista d'animes amb personatges -->

---
