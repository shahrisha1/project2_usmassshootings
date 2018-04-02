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
def mental_health_data():
    mh_yes_case = session.query(func.count(shootings.case)).group_by(shootings.year).filter(shootings.prior_signs_mental_health == "Yes")
    mh_no_case = session.query(func.count(shootings.case)).group_by(shootings.year).filter(shootings.prior_signs_mental_health == "No")
    year = session.query(shootings.year).group_by(shootings.year)
    mh_yes_fatality = session.query(func.sum(shootings.fatalities)).group_by(shootings.year).filter(shootings.prior_signs_mental_health == "Yes")
    mh_no_fatality = session.query(func.sum(shootings.fatalities)).group_by(shootings.year).filter(shootings.prior_signs_mental_health == "No")
    
    results = []

    for a,b,c,d,e in zip(mh_yes_case, mh_no_case, year, mh_yes_fatality, mh_no_fatality):
        mh_dict = {}
        mh_dict['case_count_mh_yes'] = a[0]
        mh_dict['case_count_mh_no'] = b[0]
        mh_dict['year'] = c[0]
        mh_dict['fatalities_mh_yes'] = d[0]
        mh_dict['fatalities_mh_no'] = e[0]
        results.append(mh_dict)
    return jsonify(results)

@app.route("/api/weapon-legality")
def weapon_legality_data():
    wl_yes_case = session.query(func.count(shootings.case)).group_by(shootings.year).filter(shootings.weapons_obtained_legally == 'Yes')
    wl_no_case = session.query(func.count(shootings.case)).group_by(shootings.year).filter(shootings.weapons_obtained_legally == 'No')
    year = session.query(shootings.year).group_by(shootings.year)
    wl_yes_fatality = session.query(func.sum(shootings.fatalities)).group_by(shootings.year).filter(shootings.weapons_obtained_legally == 'Yes')
    wl_no_fatality = session.query(func.sum(shootings.fatalities)).group_by(shootings.year).filter(shootings.weapons_obtained_legally == 'No')

    results = []

    for a,b,c,d,e in zip(wl_yes_case, wl_no_case, year,  wl_yes_fatality, wl_no_fatality):
        wl_dict = {}
        wl_dict['case_count_wl_yes'] = a[0]
        wl_dict['case_count_wl_no'] = b[0]
        wl_dict['year'] = c[0]
        wl_dict['fatalities_wl_yes'] = d[0]
        wl_dict['fatalities_wl_no'] = e[0]
        results.append(wl_dict)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
    raise NotImplementedError()