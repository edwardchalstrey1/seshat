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
rm -f "$table_name.sql"

# # Create an SQL script to append data to the specified table
echo "DROP TABLE IF EXISTS $table_name;" >> "$table_name.sql"
echo "CREATE TABLE $table_name (gid serial, "id" float8);" >> "$table_name.sql"
echo "ALTER TABLE $table_name ADD PRIMARY KEY (gid);" >> "$table_name.sql"
echo "SELECT AddGeometryColumn('',$table_name,'geom','4326','MULTIPOLYGON',2);" >> "$table_name.sql"

# Loop through subdirectories
for dir in "$base_dir"/*/; do
  # Extract the directory name
  subdir_name=$(basename "$dir")

  # Define the path to the .shp file (assuming the Shapefile has the same name as the subdirectory)
  shp_file="${dir}${subdir_name}.shp"

  # Use shp2pgsql to convert the Shapefile to SQL and append it to the specified table
  shp2pgsql -a -s 4326 -I "$shp_file" "$table_name" >> "$table_name.sql"
done

# Once the loop is complete, you can run the generated SQL script
echo "Run the generated SQL script ("$table_name.sql") to populate the database."
