DROP TABLE IF EXISTS macrostate_data;
CREATE TABLE macrostate_data (
    NGA TEXT,
    Polity TEXT,
    Section TEXT,
    Subsection TEXT,
    Variable TEXT,
    Value_From TEXT,
    Value_To TEXT,
    Date_From TEXT,
    Date_To TEXT,
    Fact_Type TEXT,
    Value_Note TEXT,
    Date_Note TEXT,
    Error_Note TEXT
);

-- Load data from CSV into the macrostate_data table
\copy macrostate_data FROM '../data/Macrostate_Shapefiles.2020.07/macrostate_data.csv' DELIMITER '|' CSV HEADER;
