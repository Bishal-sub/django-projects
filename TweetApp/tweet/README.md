# 🐦 Tweet App (Django)

A simple social media web application built using Django where users can register, log in, and share tweets with others.

---

## 🚀 Features

* 🔐 User Authentication (Signup, Login, Logout)
* ✍️ Create Tweets
* 🌍 View All Tweets
* 👤 User-based tweet system
* 🧩 Django built-in authentication templates

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```id="proj-structure"
.
├── templates/
│   └── registration/      # Login & auth templates
├── tweet/                 # Main project settings
├── tweetapp/              # Core app (tweets logic)
│   ├── migrations/
│   ├── templates/
│   └── models, views, urls
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash id="clone-step"
git clone https://github.com/your-username/tweet-app.git
cd tweet-app
```

---

### 2. Create virtual environment

```bash id="venv-step"
python -m venv venv
```

Activate:

* Windows:

```bash id="win-activate"
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash id="install-step"
pip install -r requirements.txt
```

---

### 4. Apply migrations

```bash id="migrate-step"
python manage.py migrate
```

---

### 5. Run server

```bash id="run-step"
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

This project uses Django’s built-in authentication system with templates located in:

```
templates/registration/
```

---

## 📌 Future Improvements

* ❤️ Like and Unlike tweets
* 💬 Comment system
* 👥 Follow users
* 🌐 REST API using Django REST Framework
* 🚀 Deployment (Render / Railway)

---

## 🤝 Contributing

Feel free to fork this repository and improve it.

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/bishal-sub

---

## ⭐ Support

If you found this useful, please ⭐ the repository!
