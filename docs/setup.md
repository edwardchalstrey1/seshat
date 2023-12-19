# Setup instructions

This page instructs software engineers how to get started working with the Django codebase and PostgreSQL database for the "core" Seshat webapp.

## Local setup

1. Ensure you have a working installation of Python 3

2. Set up a virtual environment for the project using e.g. venv or conda
    - Note: The application has been tested with Python **3.8.13**
    - Example:
        ```
            conda create --name seshat python=3.8.13
            conda activate seshat
        ```

3. Create a fork of the GitHub repo with all branches: https://github.com/MajidBenam/seshat

4. Clone your fork to your local machine

5. Ensure you have a working installation of PostgreSQL 
    - Note: The application database was originally developed with version 12, but has also been tested with PostgreSQL **version 16** (at least v14 is needed for the PostGIS extension to work)
    - <details><summary>Example instructions for macOS</summary>

        - Check if you already have PosgreSQL installed via brew:
            - `brew services list`
        - If no installation exists, follow the instructions to install https://postgresapp.com/ which **gives you PostgreSQL version 16 with PostGIS installed**.
            - Ed's note: I had a lot of trouble getting PostgreSQL 14 to start on an M1 Mac, but installing via postgresapp worked. If you have the same issue, it may be worth ensuring all traces of brew installations are removed first, e.g. run `find /opt/homebrew -name '*postgresql*'` and remove everything first
        - If you want to use brew, PostGIS will *only* work with version 14:
            - `brew install postgres@14`
            - `brew services start postgresql@14`
            - `brew install postgis`
        </details>
    - Open PostgreSQL with:
        ```
            psql postgres
        ```
    - In psql, create a default superuser called "postgres", which is needed to restore the Seshat database from backup (this may already exist):
        ```
            CREATE USER postgres SUPERUSER;
        ```

6. After PostgreSQL is installed, install the Python packages in your environment (some packages have psql as a dependency). From the top level of the `seshat` repo:
    ```
        pip install -r requirements.txt
        pip install "django-geojson [field]"
    ```

7. Restore Seshat database from dump and add PostGIS extension:
    - Note: you'll need a dump file of the Seshat database, which can be provided by one of the current developers
        ```
        createdb -U postgres <seshat_db_name>

        pg_restore -U postgres -d <seshat_db_name> /path/to/file.dump
        ```
    - Connect to the new database and add PostGIS
        ```
            psql -U postgres -d <seshat_db_name>

            CREATE EXTENSION postgis;
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

9. Set the path to your local installation of GDAL and GEOS
    - Open `seshat/settings/local.py` and edit the following variables:
        - `GDAL_LIBRARY_PATH`
        - `GEOS_LIBRARY_PATH`
    - Note: the current hardcoded paths are to the default installation by Homebrew on a Mac
    - <details><summary>Install instructions for macOS</summary>

        - `brew install gdal`
        - `brew install geos`
        </details>

10. Ensure that database migrations have run for the "core" Django app:
    ```
        python manage.py migrate core
    ```

11. If the shape data tables are not yet populated in your copy of the Seshat core database and you have access to source data, populate one or more of them with the instructions in [spatialdb.md](spatialdb.md).

12. Run Django
    ```
        python manage.py runserver
    ```

13. The webapp should be visible in a browser at http://127.0.0.1:8000/



## Azure setup

This page instructs software engineers how to set up a testing version of the Seshat website on MS Azure. You'll need an account on Azure and to have set up and credited a subscription. These are the steps followed at The Alan Turing Institute:

1. Install Azure CLI on your computer
    - <details><summary>Install instructions for macOS</summary>

        - `brew install azure-cli`
        </details>

2. Log in to Azure with the CLI, set the subscription and create a resource group called "seshat":
    ```
        az login
        az account set --subscription <subscription id>
        az group create --name seshat --location uksouth
    ```

3. Set up PostreSQL server in a new virtual network with an admin user and password
    ```
        az postgres server create --resource-group seshat --name seshatdb --location uksouth --admin-user YourAdminUsername --admin-password YourAdminPassword
    ```