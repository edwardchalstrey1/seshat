# Set up database

1. Assuming PostgreSQL is already installed (see `setup.md`), [install PostGIS](https://postgis.net/documentation/getting_started/#installing-postgis):
    <details><summary>macOS</summary>

    ```
        brew install postgis
    ```

    </details>
2. Create db and log in
    ```
        createdb -U postgres seshat_spatial
        psql -U postgres -d seshat_spatial
    ```

2. Add PostGIS extension
    ```
        CREATE EXTENSION postgis;
    ```