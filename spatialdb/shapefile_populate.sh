#!/bin/bash

# Check for the correct number of arguments
if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <base_dir> <database_name> <table_name> <data_csv>"
  exit 1
fi

# Set script arguments to variables
base_dir="$1"
database_name="$2"
table_name="$3"
data_csv="$4"

# Delete the SQL script if it already exists
rm -f "$table_name.sql"

# Create an SQL script to create the specified table
echo "DROP TABLE IF EXISTS $table_name;" >> "$table_name.sql"
echo "CREATE TABLE $table_name (gid serial, value_from text, polity text, date_from text, date_to text, id float8);" >> "$table_name.sql"
echo "ALTER TABLE $table_name ADD PRIMARY KEY (gid);" >> "$table_name.sql"
echo "SELECT AddGeometryColumn('',$table_name,'geom','4326','MULTIPOLYGON',2);" >> "$table_name.sql"

# Loop through subdirectories
while IFS=$'\t' read -r subdirectory_name polity date_from date_to value_from || [ -n "$subdirectory_name" ]; do
  subdir_path="${base_dir}/${subdirectory_name}"
  shp_file="${subdir_path}/${subdirectory_name}.shp"

  # Use shp2pgsql to convert the Shapefile to SQL and append it to the specified table
  shp2pgsql -a -s 4326 -I "$shp_file" "$table_name" >> "$table_name.sql"

  # Append the relevant information from the CSV file to the SQL script
  echo "UPDATE $table_name SET value_from = '$value_from', polity = '$polity', date_from = '$date_from', date_to = '$date_to' WHERE value_from IS NULL;" >> "$table_name.sql"
done < "$data_csv"

# Once the loop is complete, you can run the generated SQL script
echo "Run the generated SQL script ('$table_name.sql') to populate the database."
