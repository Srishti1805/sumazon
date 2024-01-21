# Sumazon Backend

![developer](https://img.shields.io/badge/Developed%20By%20%3A-Srishti%20Adkar-blue)

---
## Functions
- Register, Login, Logout Users via api.
- Register Admin users via django-admin command 
- Admin users can create, view, update and delete a product.
- A users can list, search, filter products
- A users can retrieve a individual product


## HOW TO RUN THIS PROJECT

1. Clone the repository 
    ```bash
    git clone https://github.com/Srishti1805/sumazon
    cd sumazon
    ```

2. Create virtual environment and install dependencies

    A. windows
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
    B. Linux or Mac Os
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Make migrations and migrate
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Start the server
    ```bash
    python manage.py runserver 0.0.0.0:8000 
    ```
