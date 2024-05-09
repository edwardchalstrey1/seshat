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
4. Create a new view and update the the map template with the necessary logic to use this dataset
    - views at `seshat/apps/core/views.py`
    - template e.g. `seshat/apps/core/templates/core/world_map.html`

## Cliopatria shape dataset

1. Download and unzip the Cliopatria dataset. *TODO: add a link to the published data*
2. Populate `core_videoshapefile` table
    ```
        python manage.py populate_videodata /path/to/data
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
            COALESCE(ST_Simplify(ST_Union(geom), 0.01), ST_Simplify(ST_Union(geom), 0.001)) AS geom,
            "COUNTRY"
        FROM 
            core_gadmshapefile
        GROUP BY 
            "COUNTRY";
    ```
4. To populate the `core_gadmprovinces`, go into the database (`psql -U postgres -d <seshat_db_name>`) and run the following query:
    ```{SQL}
        INSERT INTO core_gadmprovinces (geom, "COUNTRY", "NAME_1", "ENGTYPE_1")
        SELECT 
            COALESCE(ST_Simplify(ST_Union(geom), 0.01), ST_Simplify(ST_Union(geom), 0.001)) AS geom,
            "COUNTRY",
            "NAME_1",
            "ENGTYPE_1"
        FROM 
            core_gadmshapefile
        GROUP BY 
            "COUNTRY", "NAME_1", "ENGTYPE_1";
    ```

The 0.01 value is the simplification tolerance. Using a lower value will increase the resolution of the shapes used, but result in slower loading in the django app. Some smaller countries/provinces cannot be simplified with 0.01, so try 0.001.