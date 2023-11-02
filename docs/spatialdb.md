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

4. Populate database from shapefiles based on dataset:
    - Download and unzip the [Macrostate_Shapefiles](https://drive.google.com/file/d/16hC7usvuZa5KyzFg6T-_t4AJ7j_47IeM/view?usp=drive_link) dataset. Note: this is a private drive link.
    - Populate `core_macrostateshapefile` table
        ```
            python manage.py populate_macrostate /path/to/data
        ```