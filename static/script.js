var data = [{
    values: [376, 350, 555, 430, 146],
    labels: ['Manhattan', 'The Bronx', 'Brooklyn', 'Queens', 'Staten Island'],
    type: 'pie'
  }];

  var layout = {
    height: 400,
    width: 500
  };

  Plotly.newPlot('myDiv', data, layout);


//new_svg = "<svg>"+ "<path d="+park.d+" id="+"'10034'"+"</path></svg>"

// clicking on each individual svg will send you to a different sub-macro page showing an svg of the borough and every park within that borough
// using id in each svg (each id is a different zipcode), can be used as a query string for each sub-macro page
// is it possible to have a different page for each svg??
// first needs svg on click function
// then possibly needs jinja or getelementbyid
// then needs each svg of zip code individually
// look up documentation on how to save each loop as a unique file