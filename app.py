from flask import Flask, jsonify, render_template 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
import datetime
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)
#


    #
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
@app.route("/")
def welcome():
    # return render_template ("home.html")
    """List all available api routes."""
     
    return (
        f"Avalable Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start"
        
        f"- Minimum temperature, the average temperature, and the max temperature for a given start day<br/>"
        f"/api/v1.0/start/end"
        f"- Minimum temperature, the average temperature, and the max temperature for a given start-end range<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of dates and precipitation observations"""
    # Query all dates and precipitation observations last year from the measurement table
    
    prcp_results = session.query(Measurement.date, Measurement.prcp).\
                   filter(Measurement.date.between('2016-08-23', '2017-08-23')).all()
    session.close()

    precipitation= []
    for result in prcp_results:
        row = {"date":"prcp"}
        row["date"] = result[0]
        row["prcp"] = result[1]
        precipitation.append(row)

    return jsonify(precipitation)
@app.route("/api/v1.0/stations")
def stations():
   
    # Query all stations from the station table
    station_results = session.query(Station.station).all()
    session.close()

    station_list = list(np.ravel(station_results))
    return jsonify(station_list)
@app.route("/api/v1.0/tobs")
def tobs():
    tobs_results = session.query(Measurement.station, Measurement.tobs).filter(Measurement.date.between('2016-08-23', '2017-08-23')).all()
    session.close()
    
    tobs_list=[]
    for tobs in tobs_results:
        tobs_dict = {}
        tobs_dict["station"] = tobs[0]
        tobs_dict["tobs"] = float(tobs[1])
       
        tobs_list.append(tobs_dict)
    return jsonify(tobs_list)


#this is the part that uses user input and return max, min and average Temperature
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
# @app.route("/api/v1.0/")
# @app.route("/api/v1.0/")
    
def start_temp(start, end=None):
    temp_data = None
    if end:
        temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    else:
        temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
        
    session.close()
    
    # get the min/avg/max
    

    return jsonify(temp_data)




if __name__ == '__main__':
    app.run(debug=True)