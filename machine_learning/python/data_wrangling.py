"""Data Wrangling
    Apply Functions By Group In Pandas
    Apply Operations To Groups In Pandas
    Applying Operations Over pandas Dataframes
    Assign A New Column To A Pandas DataFrame
    Break A List Into N-Sized Chunks
    Breaking Up A String Into Columns Using Regex In pandas
    Construct A Dictionary From Multiple Lists
    Convert A CSV Into Python Code To Recreate It
    Convert A Categorical Variable Into Dummy Variables
    Convert A Categorical Variable Into Dummy Variables
    Convert A String Categorical Variable To A Numeric Variable
    Convert A Variable To A Time Variable In pandas
    Count Values In Pandas Dataframe
    Create A Pipeline In Pandas
    Create A pandas Column With A For Loop
    Create Counts Of Items
    Create a Column Based on a Conditional in pandas
    Creating Lists From Dictionary Keys And Values
    Crosstabs In pandas
    Delete Duplicates In pandas
    Descriptive Statistics For pandas Dataframe
    Dropping Rows And Columns In pandas Dataframe
    Enumerate A List
    Expand Cells Containing Lists Into Their Own Variables In Pandas
    Filter pandas Dataframes
    Find Largest Value In A Dataframe Column
    Find Unique Values In Pandas Dataframes
    Geocoding And Reverse Geocoding
    Geolocate A City And Country
    Geolocate A City Or Country
    Group A Time Series With pandas
    Group Data By Time
    Group Pandas Data By Hour Of The Day
    Grouping Rows In pandas
    Hierarchical Data In pandas
    Join And Merge Pandas Dataframe
    List Unique Values In A pandas Column
    Load A JSON File Into Pandas
    Load An Excel File Into Pandas
    Load Excel Spreadsheet As pandas Dataframe
    Loading A CSV Into pandas
    Long To Wide Format
    Lower Case Column Names In Pandas Dataframe
    Make New Columns Using Functions
    Map External Values To Dataframe Values in pandas
    Missing Data In pandas Dataframes
    Moving Averages In pandas
    Normalize A Column In pandas
    Pivot Tables In pandas
    Quickly Change A Column Of Strings In Pandas
    Random Sampling Dataframe
    Ranking Rows Of Pandas Dataframes
    Regular Expression Basics
    Regular Expression By Example
    Reindexing pandas Series And Dataframes
    Rename Column Headers In pandas
    Rename Multiple pandas Dataframe Column Names
    Replacing Values In pandas
    Saving A pandas Dataframe As A CSV
    Search A pandas Column For A Value
    Select Rows When Columns Contain Certain Values
    Select Rows With A Certain Value
    Select Rows With Multiple Filters
    Selecting pandas DataFrame Rows Based On Conditions
    Simple Example Dataframes In pandas
    Sorting Rows In pandas Dataframes
    Split Lat/Long Coordinate Variables Into Seperate Variables
    Streaming Data Pipeline
    String Munging In Dataframe
    Using List Comprehensions With pandas
    Using Seaborn To Visualize A pandas Dataframe
    pandas Data Structures
    pandas Time Series Basics """


def data_wrangling():
    """ doc to be created """
    """Apply Functions By Group In Pandas"""
    Preliminaries

# import pandas as pd
import pandas as pd

Create a simulated dataset
# Create an example dataframe
data = {'Platoon': ['A','A','A','A','A','A','B','B','B','B','B','C','C','C','C','C'],
       'Casualties': [1,4,5,7,5,5,6,1,4,5,6,7,4,6,4,6]}
df = pd.DataFrame(data)
df
Apply A Function (Rolling Mean) To The DataFrame, By Group

# Group df by df.platoon, then apply a rolling mean lambda function to df.casualties
df.groupby('Platoon')['Casualties'].apply(lambda x:x.rolling(center=False,window=2).mean())







