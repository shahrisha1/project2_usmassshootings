from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///shootings.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

session = Session(bind=engine)
shootings = Base.classes.shootings

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    
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

if __name__ == "__main__":
    app.run(debug=True)
    raise NotImplementedError()