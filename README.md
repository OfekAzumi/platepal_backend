# PlatePal Backend

This is the backend API for PlatePal, a delivery and takeaway management system designed for restaurants. PlatePal allows managers to oversee employees, track hours, and manage categories, dishes, customers, and orders. Employees can use the app to start/finish shifts, take orders with search and description features, and facilitate payment options including PayPal.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Models](#models)

## Features

- **Role-Based Access:** Allows managers to manage employees and operations; employees can handle shifts and orders.
- **Order Management:** Track orders with unique identifiers for easy reference.
- **Payments:** Supports cash and PayPal transactions.
- **Database Models:** Built with Django's ORM for flexible and efficient data handling.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd backend

2. **Create a virtual environment:**

   ```bash
   py -m venv .venv

3. **Activate the virtual environment and install dependencies:**

   ```bash
   .venv\Scripts\activate
   pip install -r requirements.txt

## Configuration

1. **Run migrations to set up the database:**

   ```bash
   py manage.py makemigrations
   py manage.py migrate

This will create a db.sqlite3 file to store all data.


2. **Create a superuser:**

   ```bash
   py manage.py createsuperuser

## Usage

1. **Run the server:**

   ```bash
   py manage.py runserver


2. **Access the Admin Dashboard:**

Open your browser and go to http://127.0.0.1:8000/admin to manage the backend data.


## Models

Each model has a unique code (unicode) to identify records easily:

- Category: 3-digit code (100-999)
- Dish: 4-digit code (1000-9999)
- Order: 5-digit code (10000-99999)
- Employee and Customer: 6-digit code (100000-999999)
- Typecode: Identifies the type of order, with 0 for delivery and 1 for takeaway.

## Technologies

- Python: 3.8+
- Django: 3.x
- Django REST Framework
