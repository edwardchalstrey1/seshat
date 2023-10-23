# Set up database

1. Ensure that PostgreSQL and PostGIS is already installed (see `setup.md`)
2. Create db and log in
    ```
        createdb -U postgres seshat_spatial
        psql -U postgres -d seshat_spatial
    ```

2. Add PostGIS extension
    ```
        CREATE EXTENSION postgis;
    ```