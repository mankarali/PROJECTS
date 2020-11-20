## Second Part
In this part, you will use a **second dataset** to explore the impact of **weather conditions** on police behavior during traffic stops.
### Plotting the temperature
In this exercise, you will examine the ``temperature`` columns from the ``weather`` dataset to assess whether the data seems trustworthy. First, you will print the summary statistics, and then you'll visualize the data using a **box plot**. When deciding whether the values seem reasonable, keep in mind that the temperature is measured in degrees **Fahrenheit**, not Celsius!
### INSTRUCTION
#### Data Preparation
*	Import weather.csv data set
*	Examine the data set. Tableau displays first 1000 rows by default in data grid. Get a general understanding what the dataset is about.
*	Understand the what a row-level record represents.
*	Change the workbook locale to United States. (Go to your workspace and come back to Data Source Page)
*	Identify the data types of all columns and change any if needed.
#### Data Exploration
*	Go to Sheet 1 (your workspace) and find how many records the data set has.
*	1- Create a box plot using TMIN, TAVG, TMAX.
*	2- Create a temperature difference histogram
*	The ``weather`` ``DataFrame`` contains ``20`` columns that start with ``'WT'``, each of which represents a bad weather condition. For example:
 *	``WT05`` indicates ``"Hail"``
 *	``WT11`` indicates ``"High or damaging winds"``
 *	``WT17`` indicates ``"Freezing rain"``
For every row in the dataset, each ``WT`` column contains either a ``1`` (meaning the condition was present that day) or ``NaN`` (meaning the condition was not present).
In this exercise, you will quantify ``"how bad"`` the weather was each day by counting the number of ``1`` values in each row.
 *	3 - Create a calculated column named Bad Conditions that calculates the values within WT01 to WT22. Replace the null values with zero inside the calculation. Then create a histogram that displays bad weather conditions.
*	In the previous exercise, you counted the number of bad weather conditions each day. In this exercise, you will use the counts to create a *rating system** for the weather.
The counts range from ``0`` to ``9``, and should be converted to ratings as follows:
 *   Convert ``0`` to ``'good'``
 *   Convert ``1`` through ``4`` to ``'bad'``
 *   Convert ``5`` through ``9`` to ``'worse'``
 * 4 - Create a calculated column named Rating that maps the rating. Then create a view that displays rating’s distribution.
 
  [Click here to download the Tableau Solution workbook](https://public.tableau.com/profile/mustafa.ankarali#!/vizhome/PROJECT_TPS_02/1_Create_a_Box_Plot)
