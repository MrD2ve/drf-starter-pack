# Django Rest Framework starter pack

A robust and scalable backend system built with Django REST Framework, designed to handle user authentication, billing, messaging, and asynchronous tasks. This project is containerized with Docker and integrates services like Celery, Redis, RabbitMQ, JWT authentication, SMS gateway, and email verification.

---

## 🚀 Features

- **JWT Authentication** – Secure user login and token-based access control
- **Email Verification** – Confirm email ownership during registration
- **SMS Gateway Integration** – Send OTPs or notifications via SMS
- **Billing System** – Manage payments, invoices, and transactions
- **Asynchronous Task Handling** – Background jobs using Celery, Redis, and RabbitMQ
- **Dockerized** – Easily deployable with Docker
- **Modular Architecture** – Easily extensible and organized codebase

---

## 🧱 Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Auth**: JWT (Simple JWT or djangorestframework-simplejwt)
- **Task Queue**: Celery + Redis + RabbitMQ
- **Containerization**: Docker + Docker Compose
- **Messaging**: Twilio / other SMS Gateway, Email SMTP
- **Billing**: Stripe/PayPal/Custom Integration

---

## 📦 Installation

1. Clone the Repository
```
git clone https://github.com/MrD2ve/drf-starter-pack.git
cd drf-starter-pack
```


2. Create .env file
```
Create a .env file at the root and fill it with required environment variables.
```

4. Build and Start with Docker
```
docker-compose up --build
```

📧 Contact
For any questions or collaboration inquiries, feel free to reach out at my [email] (juramurodovulugbek@gmail.com).

📄 License
This project is licensed under the MIT License.
