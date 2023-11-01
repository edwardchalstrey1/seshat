# Set up database

1. Ensure that PostgreSQL and PostGIS is already installed (see `setup.md`)
2. Add PostGIS extension to the database
    ```
        psql -U postgres -d <seshat_db_name>
        CREATE EXTENSION postgis;
    ```

3. Ensure that database migrations have run:
    ```
        python manage.py migrate
    ```

4. Populate database from shapefiles:
    ```
        python manage.py populate_spatial /path/to/data
    ```