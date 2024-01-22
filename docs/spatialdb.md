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
    - template e.g. `seshat/apps/core/templates/core/spatial_map.html`

## Macrostate shapefiles dataset

1. Download and unzip the [Macrostate_Shapefiles](https://drive.google.com/file/d/16hC7usvuZa5KyzFg6T-_t4AJ7j_47IeM/view?usp=drive_link) dataset
    - Note: this is a private drive link
2. Populate `core_macrostateshapefile` table
    ```
        python manage.py populate_macrostate /path/to/data
    ```

## RA curated dataset

1. Download and unzip the [dataset](https://drive.google.com/file/d/1qrBnwSdIM2LLBsgVWtn0k1C_cO8l2FQR/view?usp=drive_link) dataset
    - Note: this is a private drive link
2. Populate `core_videoshapefile` table
    ```
        python manage.py populate_videodata /path/to/data
    ```

This will create a row for each shape. The `end_year` of a shape is calculated to be the `start_year` of the next shape for that polity minus one, for the last shape it is the same as the `start_year`. The final shape will last just one year, but this is fine, often there will be no actual difference in the shape from previous years, this is just how the dataset represents the last year of a polity. Instead of having a shape for every single year, they have a new one each time it changes in size and for the last year.


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