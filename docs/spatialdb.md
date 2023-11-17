# Shape datasets

Ensure that the database and Django are already set up (see [setup.md](setup.md)) and all migrations have been run for the "core" Django app (`python manage.py migrate core`).

## Macrostate shapefiles dataset

1. Download and unzip the [Macrostate_Shapefiles](https://drive.google.com/file/d/16hC7usvuZa5KyzFg6T-_t4AJ7j_47IeM/view?usp=drive_link) dataset
    - Note: this is a private drive link
2. Populate `core_macrostateshapefile` table
    ```
        python manage.py populate_macrostate /path/to/data
    ```

## GADM

1. [Download](https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-gpkg.zip) the whole world GeoPackage file from the [GADM website](https://gadm.org/download_world.html).
2. Populate the `core_gadmshapefile` table
    ```
        python manage.py populate_gadm /path/to/gpkg_file
    ```
3. To populate the `core_gadmcountries`, go into the database (`psql -U postgres -d <seshat_db_name>`) and run the following query:
    ```{SQL}
        INSERT INTO core_gadmcountries (geom, "COUNTRY")
        SELECT 
            ST_Union(geom) AS geom,
            "COUNTRY"
        FROM 
            core_gadmshapefile
        GROUP BY 
            "COUNTRY";
    ```