# Django-Inventory-Management-System
This is a Django-based Inventory Management System designed for small businesses to efficiently manage their stock. Users can securely log in, track inventory, update stock quantities, add or remove products, and process orders.
## Features
- **User Authentication:** Secure session-based login
- **Inventory Management:** Add, update, or remove products from the warehouse
- **Order Management:** Place and update orders for inventory items
- **Search Functionality:** Quickly find products by code
- **Error Handling:** Custom 404 page and secure access control

## Technologies Used
- Django (Python Web Framework)
- SQLite (default Django database)
- HTML templates with Django Template Engine
- Session-based authentication

## Installation & Setup
1. Clone the repository:  
   ```bash
   git clone <repository-url>

5. Requirements install:
   ```bash
   pip install django
   
3. Apply migrations:
   ```bash
   python manage.py migrate

4. Start the development server:
   ```bash
   python manage.py runserver 8080

Open http://127.0.0.1:8080/ in your browser
