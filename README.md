# Django Projects Collection

This repository contains a growing collection of **independent Django projects**, each built to explore different features and concepts within the Django framework.

> 🚧 More projects will be added over time.

---

## 📌 Current Projects

### 📚 Book Finder

A Django project for searching and displaying book information.

**Features:**

* Search books by title or keyword
* View book details (author, description, etc.)
* External API integration (if applicable)

---

### 🐦 Tweet App

A simple Twitter-like application demonstrating CRUD operations.

**Features:**

* Create, edit, and delete tweets
* View all tweets
* Basic user interaction

---

### 🔐 Auth System

A project focused on Django authentication.

**Features:**

* User registration
* Login & logout
* Session handling
* Protected routes

---

## 🧱 Repository Structure

Each folder inside this repository is a **separate Django project**:

```bash id="3z6bnv"
django-projects/
│── book_finder/
│── tweetapp/
│── auth/
│── ... (more coming soon)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash id="k4r3lh"
git clone git@github.com:Bishal-sub/django-projects.git
cd django-projects
```

### 2. Create virtual environment

```bash id="3zwr4v"
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash id="kn9nqv"
pip install -r requirements.txt
```

> If not available:

```bash id="m7s3bz"
pip install django
```

---

## ▶️ Running a Project

Each project runs independently.

```bash id="q8u0k8"
cd project_name
python manage.py migrate
python manage.py runserver
```

Then open:

```id="9c5d9y"
http://127.0.0.1:8000/
```

---

## 🎯 Purpose

This repository is used for:

* Practicing Django development
* Building multiple standalone projects
* Exploring real-world use cases
* Strengthening backend and full-stack skills

---

## 🔮 Future Plans

* Add more Django projects
* Improve UI/UX of existing apps
* Integrate REST APIs
* Add deployment setups

---

## 🛠️ Tech Stack

* Python
* Django
* SQLite
* HTML/CSS

---

## 👤 Author

**Bishal**

---
