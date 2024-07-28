

# ElectroMart

ElectroMart is an online e-commerce platform for electronic products, built using Django. The platform allows users to browse and purchase a wide range of electronics, manage their profiles, and track their orders. Administrators can manage products, categories, and orders through a dedicated admin panel.

## Features

- User registration and authentication
- Product browsing and searching
- Shopping cart and checkout process
- Order history and tracking
- Admin panel for managing products, categories, and orders
- Responsive design for various devices

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (can be switched to PostgreSQL, MySQL, etc.)
- **Others:** Django Rest Framework (for API), Bootstrap (for styling)

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/electromart.git
   cd electromart
   ```

2. **Create and activate a virtual environment:**
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser for admin access:**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Project Structure

```
electromart/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   └── ...
├── static/
├── templates/
├── media/
└── ...
```

- `apps/`: Contains the Django apps for users, products, orders, etc.
- `static/`: Static files (CSS, JavaScript, images)
- `templates/`: HTML templates
- `media/`: Uploaded media files

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact.
![image](https://github.com/user-attachments/assets/5894f59d-f5c5-41f5-bbaf-8bcca5af7744)

![image](https://github.com/user-attachments/assets/e0bb6c99-09d1-4e6d-b893-c86b5ac670c2)
