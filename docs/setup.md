# Setup instructions

This page instructs software engineers how to get started working with the Django codebase and PostgreSQL database.

## Local setup

1. Ensure you have a working installation of Python 3

2. Set up a virtual environment for the project using e.g. venv or conda
    - Note: The application has been tested with Python **3.8.13**
    - Example:
        ```
            conda create --name seshat38 python=3.8.13
            conda activate seshat38
        ```

3. Create a fork of the GitHub repo with all branches: https://github.com/MajidBenam/seshat

4. Clone your fork to your local machine

5. Ensure you have a working installation of PostgreSQL 
    - Note: The application database was originally developed with version 12, but has also been tested with PostgreSQL **version 16**, which we need for PostGIS spatial data later on (see `spatialdb.md`)
    - <details><summary>Example instructions for macOS</summary>

        - `brew install postgres@16`
        - `brew services start postgresql@16`
        </details>
    - Open PostgreSQL with:
        ```
            psql postgres
        ```
    - In psql, create a default superuser called "postgres", which is needed to restore the Seshat database from backup:
        ```
            CREATE USER postgres SUPERUSER;
        ```

6. After PostgreSQL is installed, install the Python packages in your environment (some packages have psql as a dependency). From the top level of the `seshat` repo:
    ```
        pip install -r requirements.txt
        pip install "django-geojson [field]"
    ```

7. Restore Seshat database from dump:
    - Note: you'll need a dump file of the Seshat database, which can be provided by one of the current developers
        ```
        createdb -U postgres <seshat_db_name>

        pg_restore -U postgres -d <seshat_db_name> /path/to/file.dump
        ```
    - Connect to the new test database to make sure things are in order
        ```
            psql -U postgres -d <seshat_db_name>
        ```

8. Create a config with your database info for Django
    - Within the repo, create a file called `seshat/settings/.env` with the db connection vars
    - For example:
        ```
            NAME=<seshat_db_name>
            USER=postgres
            HOST=localhost
            PORT=5432
        ```
    - The presence of this file will ensure Django connects to your local database

9. Run Django
    ```
        python manage.py runserver
    ```

10. The webapp should be visible in a browser at http://127.0.0.1:8000/



## Production setup (AWS)

_TODO_