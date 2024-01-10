# Setup instructions

This page instructs software engineers how to get started working with the Django codebase and PostgreSQL database for the "core" Seshat webapp.

Local setup steps have been tested on an M1 Mac and on an Ubuntu VM running on the Mac.

<details><summary>Example Ubuntu VM setup on Mac</summary>

1. A quick way is to use multipass which can be installed with brew:
    ```
        brew install multipass
    ```
    - Note: the images used by Multipass don’t have a pre-installed graphical desktop
2. Create a VM (Ubuntu 22.04)
    ```
        multipass launch 22.04
    ```
    - This should create a VM called `primary` by default
3. Make sure the VM has enough resources:
    ```
        multipass stop primary
        multipass set local.primary.cpus=4
        multipass set local.primary.disk=60G
        multipass set local.primary.memory=8G
        multipass start primary
    ```
4. Then log in to the VM with `multipass shell` and install pre-requisites:
    ```
        sudo apt update
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt install python3.8 -y
        sudo apt install python3.8-venv -y
        sudo apt-get install python3.8-dev
        sudo apt-get install g++
    ```

</details>

## Local setup

1. Ensure you have a working installation of Python 3

2. Set up a virtual environment for the project using e.g. venv or conda
    - Note: The application has been tested with Python **3.8.13**
    - Conda example:
        ```
            conda create --name seshat python=3.8.13
            conda activate seshat
        ```
    - venv example:
        ```
            python3.8 -m venv seshat
            source seshat/bin/activate
        ```

3. Either create a fork of the GitHub repo with all branches: https://github.com/MajidBenam/seshat or use https://github.com/edwardchalstrey1/seshat for spatial dev work

4. Clone the repo e.g.
    ```
        git clone https://github.com/edwardchalstrey1/seshat
    ```

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
    - <details><summary>Ubuntu VM Postgres 16</summary>

        ```
            sudo apt install gnupg2 wget vim
            sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
            curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
            sudo apt update
            sudo apt install postgresql-16 postgresql-contrib-16 postgresql-16-postgis-3 -y
            sudo systemctl start postgresql
            sudo systemctl enable postgresql
        ```
        </details>
    - Open PostgreSQL with:
        ```
            psql postgres
        ```
    - In psql, create a default superuser called "postgres", which is needed to restore the Seshat database from backup (this may already exist):
        ```
            CREATE USER postgres SUPERUSER;
        ```

9. Install and configure GDAL and GEOS
    - <details><summary>Install instructions for macOS</summary>

        ```
            brew install gdal
            brew install geos
        ```
        </details>
    - <details><summary>Install instructions Ubuntu</summary>

        ```
            sudo apt-get install gdal-bin -y
            sudo apt-get install libgdal-dev
            sudo apt install libgeos++-dev libgeos3.10.2 libgeos-c1v5 libgeos-dev libgeos-doc -y
        ```
        - Note: you could first check the available libgeos version with: `sudo apt search libgeos`
        </details>
    - Open `seshat/settings/local.py` and edit the following variables:
        - `GDAL_LIBRARY_PATH`
        - `GEOS_LIBRARY_PATH`
    - Note: there are hardcoded paths in local.py for the Mac and Ubuntu instructions above included

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


### Strategy

1. Set up a VM and install things in the same way as was done above (local install) including PostgreSQL:
    - Ability to install extensions, control authentication, and configure PostgreSQL settings to meet specific application needs.
2. Mount the Azure storage account to the VM so we have access to the dumpfile that way for restoring from dump. Try with the version that has the roles included first, since we should be able to add a Superuser called "Postgres" this time, that wasn't possible when using Azure Database for PostgreSQL single server
