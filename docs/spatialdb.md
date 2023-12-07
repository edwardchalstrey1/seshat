# Shape datasets

Ensure that the database and Django are already set up (see [setup.md](setup.md)) and all migrations have been run for the "core" Django app (`python manage.py migrate core`).

To create a new shape dataset for use in the Seshat map explorer, you can do the following:

1. Create a new model for the new dataset in `seshat/apps/core/models.py`
2. Generate migration from model, and run it for your database to create the table
    ```
        python manage.py makemigrations core
        python manage.py migrate core
    ```
3. Create a new "command" at `seshat/apps/core/management/commands` which can be used to populate the db table from the dataset files
    - See the examples below
    - Add a new header on this page to document here how this works
4. Update the map template with the necessary logic to use this dataset
    - e.g. `seshat/apps/core/templates/core/spatial_map.html`

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
4. To populate the `core_gadmprovinces`, go into the database (`psql -U postgres -d <seshat_db_name>`) and run the following query:
    ```{SQL}
        INSERT INTO core_gadmprovinces (geom, "NAME_1", "ENGTYPE_1")
        SELECT 
            ST_Union(geom) AS geom,
            "NAME_1",
            "ENGTYPE_1"
        FROM 
            core_gadmshapefile
        GROUP BY 
            "NAME_1", "ENGTYPE_1";
    ```