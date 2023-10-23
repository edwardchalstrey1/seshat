#!/bin/bash

# Check for the correct number of arguments
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <base_dir> <database_name> <table_name>"
  exit 1
fi

# Set script arguments to variables
base_dir="$1"
database_name="$2"
table_name="$3"

# Delete the SQL script if it already exists
rm -f macrostate_shapefiles.sql

# # Create an SQL script to append data to the specified table
echo "CREATE TABLE $table_name (gid serial, "id" float8);" >> macrostate_shapefiles.sql
echo "ALTER TABLE "macrostate_shapefiles" ADD PRIMARY KEY (gid);" >> macrostate_shapefiles.sql
echo "SELECT AddGeometryColumn('','macrostate_shapefiles','geom','4326','MULTIPOLYGON',2);" >> macrostate_shapefiles.sql

# Loop through subdirectories
for dir in "$base_dir"/*/; do
  # Extract the directory name
  subdir_name=$(basename "$dir")

  # Define the path to the .shp file (assuming the Shapefile has the same name as the subdirectory)
  shp_file="${dir}${subdir_name}.shp"

  # Use shp2pgsql to convert the Shapefile to SQL and append it to the specified table
  shp2pgsql -a -s 4326 -I "$shp_file" "$table_name" >> macrostate_shapefiles.sql
done

# Once the loop is complete, you can run the generated SQL script
echo "Run the generated SQL script (macrostate_shapefiles.sql) to populate the database."
