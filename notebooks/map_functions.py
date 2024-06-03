import geopandas as gpd
import json

def cliopatria_gdf(cliopatria_geojson_path, cliopatria_json_path):
    """
        Load the Cliopatria shape dataset with GeoPandas and add the EndYear column to the geodataframe.
    """
    # Load the geojson file
    gdf = gpd.read_file(cliopatria_geojson_path)
    with open(cliopatria_json_path, 'r') as f:
        name_years = json.load(f)

    # Create a new column in the geodataframe
    gdf['EndYear'] = None

    # Loop through the geodataframe
    for i in range(len(gdf)):
        # Get the name of the current row
        polity_name = gdf.loc[i, 'Name']

        # Get the start year of the current row
        start_year = gdf.loc[i, 'Year']

        # Get a sorted list of the years for that name from the geodataframe
        this_polity_years = sorted(gdf[gdf['Name'] == polity_name]['Year'].unique())

        # Get the end year for a shape    
        # Most of the time, the shape end year is the year of the next shape
        # Some polities have a gap in their active years
        # For a shape year at the start of a gap, set the end year to be the shape year, so it doesn't cover the inactive period
        start_end_years = name_years[polity_name]
        end_years = [x[1] for x in start_end_years]

        polity_start_year = start_end_years[0][0]
        polity_end_year = end_years[-1]

        # Raise an error if the shape year is not the start year of the polity
        if this_polity_years[0] != polity_start_year:
            raise ValueError(f'First shape year for {polity_name} is not the start year of the polity')
        
        # Find the closest higher value from end_years to the shape year
        next_end_year = min(end_years, key=lambda x: x if x >= start_year else float('inf'))

        if start_year in end_years:  # If the shape year is in the list of polity end years, the start year is the end year
            end_year = start_year
        else:
            this_year_index = this_polity_years.index(start_year)  
            try:  # Try to use the next shape year minus one as the end year if possible, unless it's higher than the next_end_year
                next_shape_year_minus_one = this_polity_years[this_year_index + 1] - 1
                end_year = next_shape_year_minus_one if next_shape_year_minus_one < next_end_year else next_end_year
            except IndexError:  # Otherwise assume the end year of the shape is the end year of the polity
                end_year = polity_end_year

        # Set the EndYear column to the end year
        gdf.loc[i, 'EndYear'] = end_year

    return gdf