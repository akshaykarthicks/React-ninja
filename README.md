git push# Minimal & Elite To-Do App


A beautiful, minimal, and animated To-Do app built with **Django Ninja** (backend API) and **React** (frontend), inspired by Nothing OS design.
![Screenshot 2025-07-04 094853](https://github.com/user-attachments/assets/95bb38d6-9535-4264-ab20-4eb648283a04)


---

## Features
- Minimal, glassmorphic UI with smooth animations
- Fast, modern React frontend
- Django Ninja backend API (CRUD)
- Mark tasks as completed with animated checkbox
- Delete tasks instantly

---

## 1. Backend Setup (Django Ninja)

1. **Install dependencies:**
   ```bash
   pip install django django-ninja django-cors-headers
   ```
2. **Create project & app:**
   ```bash
   django-admin startproject backend
   cd backend
   python manage.py startapp todos
   ```
3. **Add to `INSTALLED_APPS` in `backend/settings.py`:**
   ```python
   INSTALLED_APPS = [
       ...
       'todos',
       'corsheaders',
   ]
   ```
   And add to `MIDDLEWARE` (top):
   ```python
   MIDDLEWARE = [
       'corsheaders.middleware.CorsMiddleware',
       ...
   ]
   CORS_ALLOW_ALL_ORIGINS = True  # For development only
   ```
4. **Create the model in `todos/models.py`:**
   ```python
   from django.db import models
   class Todo(models.Model):
       title = models.CharField(max_length=200)
       completed = models.BooleanField(default=False)
   ```
5. **Migrate:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Create API in `todos/api.py`:**
   (See project for full code. Endpoints: `/api/todos`, `/api/todos/{todo_id}`)
7. **Wire up API in `backend/urls.py`:**
   ```python
   from todos.api import api
   urlpatterns = [
       ...
       path('api/', api.urls),
   ]
   ```
8. **Run the backend:**
   ```bash
   python manage.py runserver
   ```

---

## 2. Frontend Setup (React)

1. **Create React app:**
   ```bash
   npx create-react-app frontend
   cd frontend
   ```
2. **Install dependencies:**
   (No extra dependencies needed for basic app)
3. **Replace `src/App.js` and `src/App.css` with the provided code.**
4. **Start the frontend:**
   ```bash
   npm start
   ```
5. **Open [http://localhost:3000](http://localhost:3000) in your browser.**

---

## 3. Usage
- Add a new task in the input and click **Add**.
- Mark a task as completed with the checkbox.
- Delete a task with the **Delete** button.
- All changes are synced with the backend.

---

## 4. Security & Git
- Do **not** commit `.env`, `db.sqlite3`, or any secrets to git.
- Your code (excluding secrets) is safe to push to GitHub.
- See `.gitignore` for recommended ignores.

---

## 5. Customization
- Tweak the UI in `App.css` for your own style.
- Extend the backend for authentication, user accounts, etc.

---

## 6. All Done!
You now have a modern, minimal, and animated To-Do app with a Django Ninja backend and React frontend. Enjoy!
