


# 🔐 OTP-Based User Login API (Django + JWT)

This project implements a secure OTP-based user login system using **Django**, **Django REST Framework**, and **JWT authentication**. Users can register using their email, receive a One-Time Password (OTP), verify it, and log in securely.

---

## 🚀 Features

- 📧 Email Registration
- 🔢 OTP Generation & Verification
- 🔐 JWT Token-based Authentication
- 🧪 Rate Limiting (max 3 OTP requests per 10 minutes)
- 🌐 CORS Support (frontend-backend communication)
- 💻 Responsive HTML Frontend (with clean CSS)
- 🐳 Docker-ready setup (optional)

---

## 📦 Tech Stack

- **Backend**: Django 5.2.4, Django REST Framework
- **Authentication**: djangorestframework-simplejwt
- **Database**: SQLite
- **Frontend**: HTML + CSS + JavaScript (Vanilla)
- **Email**: Mocked (printed to console)
- **Bonus**: Docker support

---

## 📁 Project Structure

user-auth-api/
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── userauth/
│   └── settings.py
├── frontend.html
├── requirements.txt
├── Dockerfile (optional)
└── manage.py



---

## 🔧 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/Ayushpatil3103/user-auth-api.git
cd user-auth-api
````

### 2. (Optional) Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run Server

```bash
python manage.py runserver
```

---

## 🖥️ Using the Frontend

Open `frontend.html` in your browser and:

1. Register with an email
2. Request OTP (check terminal for OTP)
3. Verify OTP
4. Receive JWT token!



## 📡 API Endpoints

| Method | Endpoint           | Description                |
| ------ | ------------------ | -------------------------- |
| POST   | `/api/register`    | Register user with email   |
| POST   | `/api/request-otp` | Request OTP (rate-limited) |
| POST   | `/api/verify-otp`  | Verify OTP & get JWT token |

---

## ✍️ Author

* Name: Ayush Patil
* Project Type: Internship Assignment


---

## ✅ Project Status

✅ Completed and tested successfully.

``
