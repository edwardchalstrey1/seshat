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

<!-- 3. Creating a script (and subsequent table) from an individual shapefile [with shp2pgsql](https://www.crunchydata.com/blog/loading-data-into-postgis-an-overview#shp2pgsql) results in a single row/geom in that table -->

4. Script that uses `shp2pgsql`
    ```
        cd spatialdb
        chmod +x ./macrostate_shapefiles.sh
        ./macrostate_shapefiles.sh /path/to/shapefiles_dir seshat_spatial macrostate_shapefiles
        psql -U postgres -h localhost -d seshat_spatial -f macrostate_shapefiles.sql
    ```