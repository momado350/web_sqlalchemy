## SQLAlchemy - Surfs Up! Project

#  Project requirement
Before I start the Project I did the Following:
1. Created a new repository for this project called `sqlalchemy-challenge`. 

2. Cloned the new repository to my local computer.

3. Added Jupyter notebook and `app.py` . These will be the main scripts to run for analysis.

4. Pushed all changes to GitHub.

![surfs-up.png](Images/surfs-up.png)

## Project Story
 I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning, I needed to do some climate analysis on the area. The following outlines what I need to do.

## Step 1 - Climate Analysis and Exploration

To begin,I used Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database. All of the following analysis completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* I Used [hawaii.sqlite](Resources/hawaii.sqlite) files to complete my climate analysis and data exploration.

* I picked a start date and end date for the trip. 

* I Used SQLAlchemy `create_engine` to connect to my sqlite database.

* I Usee SQLAlchemy `automap_base()` to reflect the tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis
For this Analyis I followed thses steps:

* Design a query to retrieve the last 12 months of precipitation data.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.

  ![precipitation](Images/precipitation.png)

* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis
for this one I followed these steps:

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order.

  * Which station has the highest number of observations?

  * use these functions `func.min`, `func.max`, `func.avg`, and `func.count` in the  queries.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

- - -

## Step 2 - Climate App

Now that I have completed the initial analysis, it is time to design a Flask API based on the queries that I have just developed.

* then Used Flask to create the routes.

### Application Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of the dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.




* Use Flask `jsonify` to convert your API data into a valid JSON response object.

- - -



### Temperature Analysis 

* I have Used a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Used The `calc_temps` function to calculate the min, avg, and max temperatures for the trip using the matching dates from the previous year.

* Plot the min, avg, and max temperature from  previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average
 for These Analysis these steps were followed:

* Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Used a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Making sure to use all historic TOBS that match that date string.

* Create a list of dates for the trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)




