# Shape datasets

Ensure that the database and Django are already set up (see [setup.md](setup.md)).

## Macrostate shapefiles dataset

1. Download and unzip the [Macrostate_Shapefiles](https://drive.google.com/file/d/16hC7usvuZa5KyzFg6T-_t4AJ7j_47IeM/view?usp=drive_link) dataset
    - Note: this is a private drive link
2. Populate `core_macrostateshapefile` table
    ```
        python manage.py populate_macrostate /path/to/data
    ```