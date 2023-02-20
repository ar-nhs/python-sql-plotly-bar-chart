# Plotly Bar Chart made with Python using SQL Query Data

This Python script retrieves data from a SQL Server database and creates a bar chart using Plotly to visualize the data. The SQL query is customizable to allow you to select the data you need.

![Plotly Bar Chart](/plotly_bar_chart.png)

# Requirements
- Python 3.x
- Pandas library
- SQLAlchemy library
- Plotly library

# Usage
1. Update the server and database variables in the script with your own server and database name.
```python
server = 'your_server_name'
database = 'your_database_name' 
```
2. Update the query variable in the script with your own SQL query. Make sure that the SQL query is on one line of text, otherwise the script won't work.
```python
query = "SELECT DISTINCT Admission_Date, COUNT(Patient_ID) AS Patients FROM [your_database_name].[dbo].[your_table_name] WHERE Admission_Date BETWEEN DATEADD(day, -7, GETDATE()) AND GETDATE() GROUP BY Admission_Date;"
```
3. Run the script in your terminal.
```python
python script_name.py
```
The script will connect to your SQL Server database, retrieve the data specified in your SQL query, and create a bar chart using Plotly. The bar chart will be displayed in your default web browser.

# License
This script is released under the MIT license.
