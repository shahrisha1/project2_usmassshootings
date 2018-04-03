// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 660;

// Define the chart's margins as an object
var chartMargin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 30,
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;
console.log(chartHeight);

// Select body, append SVG area to it, and set the dimensions
var svg = d3
  .select('body')
  .append('svg')
  .attr('height', svgHeight)
  .attr('width', svgWidth);

// Append a group to the SVG area and shift ('translate') it to the right and down to adhere
// to the margins set in the "chartMargin" object.
var chartGroup = svg
  .append('g')
  .attr('transform', `translate(${chartMargin.left}, ${chartMargin.top})`);

// Load data from data.csv
d3.csv('data.csv', function(error, data) {
  // Log an error if one exists
  if (error) return console.warn(error);

  // Print the data
  console.log(data);

  // Cast the data values to a number for each piece of data
  data.forEach(function(data) {
    data.laws = +data.laws;
    data.totalVictims = +data.totalVictims;
  });

  var barSpacing = 10; // desired space between each bar
  var scaleY = 10; // 10x scale on rect height

  // @TODO
  // Create a 'barWidth' variable so that the bar chart spans the entire chartWidth.
  var barWidth =
    (chartWidth - barSpacing * (data.length - 1)) / data.length;

    // scale x to chart height
var xScale = d3
.scaleLinear()
.range([0, d3.max(data)])
.domain([chartHeight, 0]);

// // scale y to chart width
var yScale = d3
.scaleBand()
.domain(data)
.range([0, chartWidth])
.padding(0.05);

// // create y axis
var yAxis = d3.axisLeft(yScale);
// var xAxis = d3.axisBottom(xScale);

// set x to the bottom of the chart
// chartGroup
//   .append('g')
//   .attr('transform', `translate(0, ${chartHeight})`)
//   .call(xAxis);

// set y to the y axis
// This syntax allows us to call the axis function
// and pass in the selector without breaking the chaining
chartGroup.append('g').call(yAxis);

// Zip the series data together (first values, second values, etc.)
var zippedData = [];
for (var i=0; i<data.laws; i++) {
  for (var j=0; j<data.totalVictims; j++) {
    zippedData.push(data[j].data[i]);
  }
}

// // Color scale
// var color = d3.scale.category20();
barHeight=20
var chartHeight = barHeight * zippedData.length + barSpacing * data.laws;


var x = d3.scale.linear()
    .domain([0, d3.max(zippedData)])
    .range([0, chartWidth]);

var y = d3.scale.linear()
    .range([chartHeight + gapBetweenGroups, 0]);

var yAxis = d3.svg.axis()
    .scale(y)
    .tickFormat('')
    .tickSize(0)
    .orient("left");

// Specify the chart area and dimensions
var chart = d3.select(".chart")
    .attr("width", spaceForLabels + chartWidth + spaceForLegend)
    .attr("height", chartHeight);

// Create bars
var bar = chart.selectAll("g")
    .data(zippedData)
    .enter().append("g")
    .attr("transform", function(d, i) {
      return "translate(" + spaceForLabels + "," + (i * barHeight + barSpacing * (0.5 + Math.floor(i/data.series.length))) + ")";
    });

// Create rectangles of the correct width
bar.append("rect")
    .attr("fill", function(d,i) { return color(i % data.series.length); })
    .attr("class", "bar")
    .attr("width", x)
    .attr("height", barHeight - 1);

// Add text label in bar
bar.append("text")
    .attr("x", function(d) { return x(d) - 3; })
    .attr("y", barHeight / 2)
    .attr("fill", "red")
    .attr("dy", ".35em")
    .text(function(d) { return d; });

// Draw labels
bar.append("text")
    .attr("class", "label")
    .attr("x", function(d) { return - 10; })
    .attr("y", groupHeight / 2)
    .attr("dy", ".35em")
    .text(function(d,i) {
      if (i % data.series.length === 0)
        return data.labels[Math.floor(i/data.series.length)];
      else
        return ""});

chart.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(" + spaceForLabels + ", " + -gapBetweenGroups/2 + ")")
      .call(yAxis);

// Draw legend
var legendRectSize = 18,
    legendSpacing  = 4;

var legend = chart.selectAll('.legend')
    .data(data.series)
    .enter()
    .append('g')
    .attr('transform', function (d, i) {
        var height = legendRectSize + legendSpacing;
        var offset = -gapBetweenGroups/2;
        var horz = spaceForLabels + chartWidth + 40 - legendRectSize;
        var vert = i * height - offset;
        return 'translate(' + horz + ',' + vert + ')';
    });

legend.append('rect')
    .attr('width', legendRectSize)
    .attr('height', legendRectSize)
    .style('fill', function (d, i) { return color(i); })
    .style('stroke', function (d, i) { return color(i); });

legend.append('text')
    .attr('class', 'legend')
    .attr('x', legendRectSize + legendSpacing)
    .attr('y', legendRectSize - legendSpacing)
    .text(function (d) { return d.label; });







//   // Create code to build the bar chart using the data.
//   chartGroup
//     .selectAll('.bar')
//     .data(data)
//     .enter()
//     .append('rect')
//     .classed('bar', true)
//     .attr('width', d => barWidth)
//     .attr('height', d => d.laws * scaleY)
//     .attr('x', (d, i) => i * (barWidth + barSpacing))
//     .attr('y', d => chartHeight - d.laws * scaleY);
});
