# Library Management System

A Django-based library management platform backed by MySQL, featuring complete CRUD operations for Books, Authors, Publishers, Genres, Book Copies, and Reviews via the Django Admin panel.

## Features
- **Backend**: Django 6.1 with  database driver.
- **Database**: MySQL 8.0 relational schema with secure  configuration.
- **Admin Panel**: Customized  interface with search, filters, inline relations, and calculated fields.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/my_library.git
   cd my_library
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows Git Bash
   ```

3. **Install dependencies:**
   ```bash
   pip install django pymysql python-dotenv
   ```

4. **Configure environment variables ():**
   Create a  file in the root directory:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=library_db
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

5. **Run migrations:**
   ```bash
   python library_system/manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python library_system/manage.py runserver
   ```

7. Visit  in your browser.
