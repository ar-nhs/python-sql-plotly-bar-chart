# This Python script connects to a SQL Server database, executes a
# SQL query on that database, and then visualizes the data in a bar 
# chart using Plotly. 

# Author: Adam Ross
# Date: 2023-02-20

# Imports required Python modules for the script to work: 
# Pandas, SQLAlchemy, Plotly graph objects, and Plotly offline.
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objs as go
from plotly.offline import plot

# Defines server and database variables, which are used to 
# create the connection string for the SQL Server database.
server = 'your_server_name'
database = 'your_database'

# Create SQL Server connection string
driver = 'SQL+Server'
connection_string = f"mssql+pyodbc://{server}/{database}?driver={driver}"

# Attempts to connect to the database using SQLAlchemy,
# and prints a success or error message depending on the outcome.
try:
    engine = create_engine(
        f"mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver={driver}")
    conn = engine.connect()
    print("Database connection successful")
except Exception as e:
    print("Error connecting to database:", e)

# Defines a SQL query, replace the query with your own.
query = "SELECT DISTINCT Column_A, COUNT(Column_B) AS Column B FROM [your_database_name].[dbo].[your_table_name];"
# Executes the SQL query on the database using SQLAlchemy and stores 
# the result as a Pandas dataframe.
df = pd.read_sql_query(query, con=engine)

# Uses the Plotly module to create a bar chart using the data from the Pandas dataframe.
# Remember to amend Column_A and Column_B to the names of the columns used in your SQL query.
fig = go.Figure()
fig.add_trace(go.Bar(x=df['Column_A'], y=df['Column_B']))

# Set chart title and axis labels
fig.update_layout(title='Your Chart Title',
                  xaxis_title='X Axis Title',
                  yaxis_title='Y Axis')

# Show the chart
plot(fig)
