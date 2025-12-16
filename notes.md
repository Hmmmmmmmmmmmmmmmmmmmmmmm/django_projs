# Django Notes

This MD will contain all the details I find important throughout learning to use Django.

## Basic Structure of a Django Project

To create a project, run:

django-admin startproject project_name

The structure of it will be:

new_proj/
├── .gitignore
├── project_1/
│   ├── manage.py
│   └── project_1/
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
└── new_venv/       ← ignored

### Explanation of Each File/Folder

**manage.py**
A command-line utility that lets you interact with your Django project.

You can run commands like:

python manage.py runserver
python manage.py migrate
python manage.py startapp appname

**Inner `project_1/` folder**
This is the actual Python package for your project (same name as your project).

- `__init__.py`
  Marks this directory as a Python package. Usually empty.

- `settings.py`
  Configuration for your Django project: database settings, installed apps, middleware, templates, static files, etc.
  This is where most of your project-wide settings live.

- `urls.py`
  The “table of contents” for your project’s URLs.
  You define which URLs map to which views here.

- `asgi.py`
  Entry point for ASGI-compatible web servers (for async features and channels).
  Mostly used for deployment with asynchronous servers.

- `wsgi.py`
  Entry point for WSGI-compatible web servers (classic sync servers).
  Also used mainly for deployment.

### In Short

- `manage.py` → command-line utility
- Inner project folder → Python package containing project settings and server entry points
- `settings.py` → configuration
- `urls.py` → URL routing
- `asgi.py` / `wsgi.py` → deployment entry points

# Django `runserver` Notes

Running:

python manage.py runserver

### What it does
- Starts a development server on your local machine (default: 127.0.0.1:8000).
- Lets you view your Django project in a browser while developing.
- Automatically reloads when Python code or templates change.

**Note:** This server is only for development, not production.

### Basic Usage
- Default:
  python manage.py runserver
  → Opens at http://127.0.0.1:8000/

- Custom port:
  python manage.py runserver 8080
  → Runs at http://127.0.0.1:8080/

- Custom IP & port:
  python manage.py runserver 0.0.0.0:8000
  → Makes the server accessible on the local network.

### Behind the Scenes
When you run `runserver`:
1. Django reads `settings.py`.
2. Sets up URL routing from `urls.py`.
3. Loads apps from `INSTALLED_APPS`.
4. Starts listening for HTTP requests.

When a request comes in:
1. URL is matched via `urls.py`.
2. Corresponding view is called.
3. Template (if any) is rendered.
4. Response is sent back to the browser.
