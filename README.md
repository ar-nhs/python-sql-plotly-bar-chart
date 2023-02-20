# Plotly Bar Chart made with Python using SQL Query Data

This Python script retrieves data from a SQL Server database and creates a bar chart using Plotly to visualize the data. The SQL query is customizable to allow you to select the data you need.

![Plotly Bar Chart](/plotly_bar_chart.png)

# Requirements
- Python 3.x
- Pandas library
- SQLAlchemy library
- Plotly library

# Usage
1. Install the libraries specified in the requirements.
```python
pip install pandas SQLAlchemy plotly
```
2. Update the server and database variables in the script with your own server and database name.
```python
server = 'your_server_name'
database = 'your_database_name' 
```
3. Update the query variable in the script with your own SQL query. Make sure that the SQL query is on one line of text, otherwise the script won't work.
```python
query = "SELECT DISTINCT Column_A, COUNT(Column_B) AS Column B FROM [your_database_name].[dbo].[your_table_name];"
```
4. Amend the column names in line 43 of the script.
```python
fig.add_trace(go.Bar(x=df['Column_A'], y=df['Column_B']))
```
5. Change the chart title, and also the X & Y Axis titles.
```python
fig.update_layout(title='Your Chart Title',
                  xaxis_title='X Axis Title',
                  yaxis_title='Y Axis')
```
6. Run the script in your terminal.
```python
python script_name.py
```
The script will connect to your SQL Server database, retrieve the data specified in your SQL query, and create a bar chart using Plotly. The bar chart will be displayed in your default web browser.

# License
This script is released under the MIT license.
