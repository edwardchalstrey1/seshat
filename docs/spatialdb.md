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

3. Run script that uses `shp2pgsql` to populate a table in the db with one row per shape. Expects `shapefiles_dir` to contain subdirectories that each contain a single `.shp` file, named the same as the subdirectory and "Polity", "Value.From", "Date.From" and "Date.To" to be columns in the tab delimited `.csv`:
    ```
        cd spatialdb

        chmod +x ./shapefile_populate.sh

        ./shapefile_populate.sh /path/to/shapefiles_dir seshat_spatial <table name> <csv>
        
        psql -U postgres -h localhost -d seshat_spatial -f <table_name>.sql
    ```