

var url = "/weapons";
d3.json(url, (error, data) => {
  if (error) return console.log(error);
  console.log(data)


  new Chart(document.getElementById("bar-chart"), {
    type: 'doughnut',
    data: {
      labels: ["Yes", "No", "Unknown"],
      datasets: [
        {
          // label: 
          backgroundColor: ["#78281F", "#EDBB99","#808080"],
          data: [data[0],data[1], data[2]]
        }
      ]
    },
    options: {
      responsive: false,
      // maintainAspectRatio: false,
      legend: { display: true },
      title: {
        display: true,
        text: 'Weapons Obtained Legally?'
      }
    }
     
});



  // console.log(data);
  // console.log(data[0]);
});

var url = "/weaponsused";
d3.json(url, (error, data) => {
  if (error) return console.log(error);


  new Chart(document.getElementById("bar-chart1"), {
    type: 'bar',
    data: {
      labels: ['Semi Automatic Handgun','Handgun','Rifle','Shotgun','Semi Automatic Rifle','Long Gun'],
      datasets: [
        {
          // label: "Yes",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850", "#3e95cd"],
          data: [data['Semi Automatic Handgun'], data['Handgun'],data['Rifle'],data['Shotgun'], data['Semi Automatic Rifle'],data['Long Gun']]
        }
      ]
    },
    options: {
      responsive: false,
      // maintainAspectRatio: false,
      legend: { display: false },
      title: {
        display: true,
        text: 'Weapons Type Used'
      }
    }
});



  // console.log(data);
  // console.log(data['Handgun']);
});


var url = "/state";
d3.json(url, (error, data) => {
  if (error) return console.log(error);

  // console.log(data);

  var url = "/percent";
d3.json(url, (e, d) => {
  if (error) return console.log(error);

  // console.log(d);


  new Chart(document.getElementById("bar-chart2"), {
    type: 'horizontalBar',
    data: {
      labels: data,
      datasets: [
        {
          label: "My First dataset",
          fillColor: "rgba(54, 162, 235, 0.2)",
          strokeColor: "rgba(220,220,220,0.8)",
          highlightFill: "rgba(220,220,220,0.75)",
          highlightStroke: "rgba(220,220,220,1)",
          // label: "Yes",
          backgroundColor: ["#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd",],
          data: d
        }
      ]
    },
    options: {
      legend: { display: false },
      responsive: false,
      // maintainAspectRatio: false,
      title: {
        display: true,
        text: 'Gun Ownership By State'
      }
    }
});


  // console.log(data);
  // console.log(data['Handgun']);


})

});


var url = "/state_name";
d3.json(url, (error, data) => {
  if (error) return console.log(error);

  console.log(data);

  var url = "/laws";
d3.json(url, (e, d) => {
  if (error) return console.log(error);

  console.log(d);

  var url = "/victims";
  d3.json(url, (e, d1) => {
    if (error) return console.log(error);
  
    console.log(d1);



  new Chart(document.getElementById("bar-chart3"), {
    type: 'horizontalBar',
    data: {
      labels: data,
      datasets: [
        {
          label: "Gun Laws by State",
          fillColor: "#3e95cd",
          strokeColor: "rgba(220,220,220,0.8)",
          highlightFill: "rgba(220,220,220,0.75)",
          highlightStroke: "rgba(220,220,220,1)",
          // label: "Yes",
          backgroundColor: ["#3e95cd","#3e95cd", "#3e95cd" , "#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd","#3e95cd"],
          data: d
        }, 
        {
          label: "Victims by State",
          fillColor: "rgba(255, 206, 86, 0.2)",
          strokeColor: "rgba(220,220,220,0.8)",
          highlightFill: "rgba(220,220,220,0.75)",
          highlightStroke: "rgba(220,220,220,1)",
          // label: "Yes",
          backgroundColor: ["#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00","#FF8C00"],
          data: d1
        }
        
      ]
    },
    options: {
      responsive: false,
      // maintainAspectRatio: false,
      legend: { display: true },
      title: {
        display: true,
        text: 'Gun Laws Vs Victims'
      }
    }
});


  // console.log(data);
  // console.log(data['Handgun']);


})

})

});

// function init() {
//   var data = [
//     {
//       values: [19, 26, 55, 88],
//       labels: ['Spotify', 'Soundcloud', 'Pandora', 'Itunes'],
//       type: 'horizontal-bar',
//     },
//   ];
//   var layout = {
//     height: 600,
//     width: 800,
//   };
//   Plotly.plot('bar', data, layout);
// }
// function updatePlotly(newdata) {
//   var PIE = document.getElementById('pie');
//   Plotly.restyle(PIE, 'values', [newdata]);
// }
// function getData(dataset) {
//   var data = [];
//   switch (dataset) {
//     case 'dataset1':
//       data = [1, 2, 3, 39];
//       break;
//     case 'dataset2':
//       data = [10, 20, 30, 37];
//       break;
//     case 'dataset3':
//       data = [100, 200, 300, 23];
//       break;
//     default:
//       data = [30, 30, 30, 11];
//   }
//   updatePlotly(data);
// }
// init();


new Chart(document.getElementById("donut"), {
  type: 'doughnut',
  data: {
    labels: ["Other", "Workplace", "School", "Miltary", "Relegiius", "Airport"],
    datasets: [
      {
        // label: 
        backgroundColor: ["#626d00", "#626d7e", "#808080", "#61597e", "#614148", "#655848"],
        data: [43, 30, 26, 5, 5, 1]
      }
    ]
  },
  options: {
    responsive: false,
    // maintainAspectRatio: false,
    legend: { display: true },
    title: {
      display: true,
      // text: 'Venue?'
    }
  }

});