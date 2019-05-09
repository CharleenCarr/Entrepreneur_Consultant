// This function reformat the dataset into a dictionary array list, 
// sort, and slice the 1st top 10 rows
function filterData(dataset) {
  dList = [];
 
  for (i=0; i < dataset.name.length; i++) { 
  //  console.log(`ROw${i}]: ${results.otu_ids[i]}, ${results.sample_values[i]}, ${results.otu_labels[i]}`) ;
    dict = {};
    dict["region"] = dataset.name[i];
    dict["percent"] = dataset.percent[i];
    dList.push(dict);
  }
}
  
// This function set city's images & link
function buildCharts() {
  url = "/population" 
  d3.json(url).then((results) => {
    // console.log(results)

    // Default hoverinfo - all
    var data = {
      labels: results.name,
      values: results.percent,
      type: 'pie'
    }

    var layout = {
      title: "<b>Population By Region 2018, USA</b>",
      width: 500,
      height: 500     
    }

    Plotly.newPlot("popie", [data], layout, {responsive: true});
  });
}

buildCharts();