# SkoolProject

> Django-based school management application (SkoolProject).

## Overview

SkoolProject is a Django web application to manage school-related data (students, authentication, admin, and basic UI). The repo contains multiple Django apps including `home_auth`, `skool`, and `student` plus static assets and templates.

## Requirements

- Python 3.10+ (use the virtual environment in `myenv` or create your own)
- See `requirement.txt` for Python packages

## Quickstart (Windows)

1. Activate virtualenv (if using the included `myenv`):

```
myenv\Scripts\activate
```

2. Install dependencies:

```
pip install -r requirement.txt
```

3. Apply database migrations:

```
python manage.py migrate
```

4. Create a superuser (admin):

```
python manage.py createsuperuser
```

5. Run the development server:

```
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Testing

Run the test suite:

```
python manage.py test
```

## Project Structure (high level)

- `SkoolProject/` — Django project settings and entry points ([SkoolProject/settings.py](SkoolProject/settings.py)).
- `home_auth/` — authentication views and models.
- `skool/` — core school app.
- `student/` — student management (models, views, templates).
- `templates/` — HTML templates used by the apps.
- `static/` — static assets (CSS, JS, images).
- `db.sqlite3` — default development SQLite database (auto-created).

## Configuration

- Secret keys and production settings: review `SkoolProject/settings.py` before deploying.
- Use environment variables for sensitive data in production.

## Admin

After creating a superuser, access the admin at `/admin/`.

## Contributing

- Open issues for bugs or feature requests.
- Create pull requests for proposed changes.

## Credits

This README was generated to help developers get started with SkoolProject quickly.

---

