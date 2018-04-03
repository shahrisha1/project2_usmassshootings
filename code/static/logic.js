function totalcase_chart(){
Plotly.d3.json("/api", (error, response)=>{
    if (error) throw error;
    console.log(response);
    var year = [];
    var fatality = [];
    var case_count = [];
    for (var i = 0; i < response.length; i++){
        year.push(response[i].year);
        fatality.push(response[i].total_fatalities);
        case_count.push(response[i].case_count);
    };
    console.log(year);
    var trace1 = {    
        x: year,
        y: case_count,
        mode: 'lines+markers',
        text: poptext(fatality),
        marker: {
          size: fatality,
          sizeref: 0.09,
          sizemode: 'area',
          color: 'rgba(230, 46, 0, .7)'
        },
        name:"Total Fatalities"
      };
      var data = [trace1];

      var layout = {
        showlegend: true,
        title: 'Number of US Mass Shootings from 1982 to 2018',
        xaxis: {title: 'Years'},
        yaxis:{title: 'Number of Incidents'},
        height: 600,
        width: 900
      };
      
      Plotly.newPlot('plot-id', data, layout);
});
};

function mentalhealth_chart(){
Plotly.d3.json("api/mental-health", (error, response)=>{
    if (error) throw error;
    console.log(response);
    var year_yes = [];
    var year_no = [];
    var fatality_yes = [];
    var fatality_no = []
    var case_count_yes = [];
    var case_count_no = [];
    for (var i = 0; i < response.length; i++){
        if (typeof (response[i].case_count_mh_yes) !== 'undefined') {
        year_yes.push(response[i].year)
        case_count_yes.push(response[i].case_count_mh_yes);
        fatality_yes.push(response[i].fatalities_mh_yes);
        };
        if (typeof (response[i].case_count_mh_no) !== "undefined"){
        year_no.push(response[i].year)
        case_count_no.push(response[i].case_count_mh_no);
        fatality_no.push(response[i].fatalities_mh_no);
        };

    };
    var trace1 = {
        x: year_yes,
        y: case_count_yes,
        mode: 'lines+markers',
        text: poptext(fatality_yes),
        marker: {
          size: fatality_yes,
          sizeref: 0.05,
          sizemode: 'area',
          color: 'rgba(255, 71, 26, 0.8)'
        },
        name: 'Fatalities (Mental Illness: Yes)' 
      };

      var trace2 = {
        x: year_no,
        y: case_count_no,
        mode: 'lines+markers',
        text: poptext(fatality_no),
        marker: {
          size: fatality_no,
          sizeref: 0.05,
          sizemode: 'area',
          color: 'rgba(10, 84, 0, .7)'
        },
        name: 'Fatalities (Mental Illness: No)'
      };
      var data = [trace1, trace2];

      var layout = {
        title: 'Number of US Mass Shooting from 1982 to 2018 (Confirmed Mental Health)',
        xaxis: {title: 'Years'},
        yaxis:{title: 'Number of Incidents'},
        height: 600,
        width: 900
      };
      
      Plotly.newPlot('plot-id', data, layout);
});
};

function weaponlegal_chart(){
Plotly.d3.json("api/weapon-legality", (error, response)=>{
    if (error) throw error;
    console.log(response);
    var year_yes = [];
    var year_no = [];
    var fatality_yes = [];
    var fatality_no = []
    var case_count_yes = [];
    var case_count_no = [];
    for (var i = 0; i < response.length; i++){
      if (typeof (response[i].case_count_wl_yes) !== 'undefined'){  
        year_yes.push(response[i].year);
        case_count_yes.push(response[i].case_count_wl_yes);
        fatality_yes.push(response[i].fatalities_wl_yes);
       };
      if (typeof (response[i].case_count_wl_no) !== 'undefined'){  
        year_no.push(response[i].year);
        case_count_no.push(response[i].case_count_wl_no);
        fatality_no.push(response[i].fatalities_wl_no);
      };
    };
    var trace1 = {
        x: year_yes,
        y: case_count_yes,
        mode: 'lines+markers',
        text: poptext(fatality_yes),
        marker: {
          size: fatality_yes,
          sizeref: 0.05,
          sizemode: 'area',
          color:'rgba(255, 71, 26, 0.8)'
        },
        name: 'Fatalities (Weapon Obtained Legally)'
      };

      var trace2 = {
        x: year_no,
        y: case_count_no,
        mode: 'lines+markers',
        text: poptext(fatality_no),
        marker: {
          size: fatality_no,
          sizeref: 0.05,
          sizemode: 'area',
          color: 'rgba(12, 100, 0, .5)'
        },
        name: 'Fatalities (Weapon Obtained Illegally)'
     };
      var data = [trace1, trace2];

      var layout = {
        title: 'Number of US Mass Shooting from 1982 to 2018 (Confirmed Weapon Legality)',
        xaxis: {title: 'Years'},
        yaxis:{title: 'Number of Incidents'},
        height: 600,
        width: 1000
      };
      
      Plotly.newPlot('plot-id', data, layout);
});
};
totalcase_chart();

function getData(dataset) {
    console.log('Dataset:', dataset);

    switch (dataset) {
      case 'dataset1':
        console.log('dataset 1');
        mentalhealth_chart();
        break;
      case 'dataset2':
        console.log('dataset 2');
        weaponlegal_chart();
        break;
      
      default:
        console.log('default');
        totalcase_chart();
        break;
    }};

function poptext(alist){
  var text_list = []
  for (var i=0; i < alist.length; i++){
    text_list.push("'Fatalities: " + alist[i]+"'");
  } 
  return text_list;
};