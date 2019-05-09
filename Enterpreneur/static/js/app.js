// This function set city's images & link
function buildCharts() {
  url = "/population" 
  d3.json(url).then((results) => {
    console.log(results)
//     // Build a Pie Chart
//     dataset = filterData(results);
//     // console.log(dataset);   dataset.map(row => row.otu_labels)

//     // Default hoverinfo - all
//     var pie_data = {
//       labels: dataset.map(row => row.otu_ids),
//       values: dataset.map(row => row.smpl_values),
//       hovertext: dataset.map(row => row.otu_labels),
//       type: 'pie'
//     }

//     var pie_Layout = {
//       title: "<b>Sample's Top 10 Results</b>",
//       width: 500,
//       height: 500     
//     }

//     Plotly.newPlot("pie", [pie_data], pie_Layout, {responsive: true});
  });
}

