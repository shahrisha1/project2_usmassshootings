# import necessary libraries
from sqlalchemy import func
from flask import Flask, render_template, jsonify
import database as data
import json
import numpy
import weaponsused_count as w
import gun_ownership as g
import laws_victims as lv
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



#database setup
engine = create_engine("sqlite:///shootings.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

#save tables as variables
session = Session(engine)
shootings = Base.classes.shootings


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


# Query the database and send the jsonified results

@app.route("/")
def home():
    """Return the dashboard homepage."""
    return render_template("index.html")


@app.route("/weapons_obtained", methods=['GET','POST'])
def weapons_obtained():
    weapons_df=data.complete_shootings_df.weapons_obtained_legally.value_counts()
    weapons=weapons_df.astype(float).to_dict()
    return jsonify(weapons)


@app.route("/weapons", methods=['GET','POST'])
def weapons():
    weapons_df=data.complete_shootings_df.weapons_obtained_legally.value_counts()
    weapons=weapons_df.astype(float).to_dict()
    return jsonify(list(weapons.values()))


@app.route("/weaponsused", methods=['GET','POST'])
def weapons_used():
    return jsonify(w.weapons_count_dict)


@app.route("/gunowner", methods=['GET','POST'])
def gunowner():
    return jsonify(g.gun_owners_state_dict)


@app.route("/state", methods=['GET','POST'])
def state():
    return jsonify(list(g.gun_owners_state_dict.keys()))


@app.route("/percent", methods=['GET','POST'])
def percentage_state():
    return jsonify(list(g.gun_owners_state_dict.values()))


@app.route("/state_name", methods=['GET','POST'])
def state_name():
    return jsonify(lv.state)


@app.route("/laws", methods=['GET','POST'])
def laws():
    laws=list(map(float, lv.laws))
    return jsonify(laws)


@app.route("/victims", methods=['GET','POST'])
def victims():
    victims=list(map(float, lv.victims))
    return jsonify(victims)


######HARRYCODE#####

@app.route("/api")
def shooting_data():
    data = session.query(func.count(shootings.case).label('case_count'), shootings.year, func.sum(shootings.fatalities).label('fatalities') ).group_by(shootings.year).all()
    results = []
    for row in data:
        data_dict = {}
        data_dict['year']= row.year
        data_dict['case_count'] = row.case_count
        data_dict['total_fatalities'] = row.fatalities
        results.append(data_dict)
    return jsonify(results)

@app.route("/api/mental-health")
def mental_health_yes_data():
    mh_yes_query = session.query(func.count(shootings.case).label('mh_yes_case'), shootings.year, func.sum(shootings.fatalities).label('mh_yes_fatality') ).group_by(shootings.year).filter(shootings.prior_signs_mental_health == "Yes")
    mh_no_query = session.query(func.count(shootings.case).label('mh_no_case'), shootings.year, func.sum(shootings.fatalities).label('mh_no_fatality') ).group_by(shootings.year).filter(shootings.prior_signs_mental_health == "No")
    results = []
    for i in mh_yes_query:
        mh_dict = {}
        mh_dict['case_count_mh_yes'] = i.mh_yes_case
        mh_dict['year'] = i.year
        mh_dict['fatalities_mh_yes'] = i.mh_yes_fatality
        results.append(mh_dict)
    for j in range(len(results)):
        for k in mh_no_query:
            if (k.year == results[j]['year']):
                results[j]['case_count_mh_no'] = k.mh_no_case
                results[j]['fatalities_mh_no'] = k.mh_no_fatality
    return jsonify(results)

@app.route("/api/weapon-legality")
def weapon_legality_data():
    wl_yes_query = session.query(func.count(shootings.case).label('wl_yes_case'), shootings.year, func.sum(shootings.fatalities).label('wl_yes_fatality') ).group_by(shootings.year).filter(shootings.weapons_obtained_legally == 'Yes')
    wl_no_query = session.query(func.count(shootings.case).label('wl_no_case'), shootings.year, func.sum(shootings.fatalities).label('wl_no_fatality') ).group_by(shootings.year).filter(shootings.weapons_obtained_legally == 'No')
    results = []
    for i in wl_yes_query:
        mh_dict = {}
        mh_dict['case_count_wl_yes'] = i.wl_yes_case
        mh_dict['year'] = i.year
        mh_dict['fatalities_wl_yes'] = i.wl_yes_fatality
        results.append(mh_dict)
    for j in range(len(results)):
        for k in wl_no_query:
            if (k.year == results[j]['year']):
                results[j]['case_count_wl_no'] = k.wl_no_case
                results[j]['fatalities_wl_no'] = k.wl_no_fatality
    return jsonify(results)
   

# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/api")
# def shooting_data():
#     data = session.query(func.count(shootings.case).label('case_count'), shootings.year, func.sum(
#         shootings.fatalities).label('fatalities')).group_by(shootings.year).all()
#     results = []
#     for row in data:
#         data_dict = {}
#         data_dict['year'] = row.year
#         data_dict['case_count'] = row.case_count
#         data_dict['total_fatalities'] = row.fatalities
#         results.append(data_dict)
#     return jsonify(results)


# @app.route("/api/mental-health")
# def mental_health_data():
#     mh_yes_case = session.query(func.count(shootings.case)).group_by(
#         shootings.year).filter(shootings.prior_signs_mental_health == "Yes")
#     mh_no_case = session.query(func.count(shootings.case)).group_by(
#         shootings.year).filter(shootings.prior_signs_mental_health == "No")
#     year = session.query(shootings.year).group_by(shootings.year)
#     mh_yes_fatality = session.query(func.sum(shootings.fatalities)).group_by(
#         shootings.year).filter(shootings.prior_signs_mental_health == "Yes")
#     mh_no_fatality = session.query(func.sum(shootings.fatalities)).group_by(
#         shootings.year).filter(shootings.prior_signs_mental_health == "No")

#     results = []

#     for a, b, c, d, e in zip(mh_yes_case, mh_no_case, year, mh_yes_fatality, mh_no_fatality):
#         mh_dict = {}
#         mh_dict['case_count_mh_yes'] = a[0]
#         mh_dict['case_count_mh_no'] = b[0]
#         mh_dict['year'] = c[0]
#         mh_dict['fatalities_mh_yes'] = d[0]
#         mh_dict['fatalities_mh_no'] = e[0]
#         results.append(mh_dict)
#     return jsonify(results)


# @app.route("/api/weapon-legality")
# def weapon_legality_data():
#     wl_yes_case = session.query(func.count(shootings.case)).group_by(
#         shootings.year).filter(shootings.weapons_obtained_legally == 'Yes')
#     wl_no_case = session.query(func.count(shootings.case)).group_by(
#         shootings.year).filter(shootings.weapons_obtained_legally == 'No')
#     year = session.query(shootings.year).group_by(shootings.year)
#     wl_yes_fatality = session.query(func.sum(shootings.fatalities)).group_by(
#         shootings.year).filter(shootings.weapons_obtained_legally == 'Yes')
#     wl_no_fatality = session.query(func.sum(shootings.fatalities)).group_by(
#         shootings.year).filter(shootings.weapons_obtained_legally == 'No')

#     results = []

#     for a, b, c, d, e in zip(wl_yes_case, wl_no_case, year,  wl_yes_fatality, wl_no_fatality):
#         wl_dict = {}
#         wl_dict['case_count_wl_yes'] = a[0]
#         wl_dict['case_count_wl_no'] = b[0]
#         wl_dict['year'] = c[0]
#         wl_dict['fatalities_wl_yes'] = d[0]
#         wl_dict['fatalities_wl_no'] = e[0]
#         results.append(wl_dict)
#     return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)
    raise NotImplementedError()
