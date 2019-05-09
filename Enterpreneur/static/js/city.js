//  // This function clear all charts & data
// function clearAll(){
//     var divList = ["#pie", "#bubble", "#gauge", "#smpl-meta"];
//     divList.forEach(div => {
//       d3.select(div).selectAll("*").remove();
//     })
//   }
  
// This function rebuild all charts & data on selection change 
function optionChanged(name) { 
    // alert(name);
    get_Cityfiles(name);
}

// This function set city's images & link
function get_Cityfiles(name) {
    list = ["categories", "word"];

    // alert(name);
    url = "/select/" + name
    d3.json(url).then(function(results) {
        // console.log(results);

        for (var i = 0; i < list.length; i++) {
            // console.log(list[i]);
            // if img.toLowerCase().indexOf(link) {

        }
 
        // Object.entries(results).forEach(([id, value]) => {
        //     console.log(value);
        //         value.forEach((item) => {console.log(item)}

        //     )
        // });   
    

        Object.entries(results).forEach(([id, item]) => {
            console.log(id);
            item.forEach(img => {
                for (var i = 0; i < list.length; i++) {
                    m = String(img);
                    console.log(m);
                    console.log(list[i]);
                    // if m.includes(list[i]) {

                    // }
                }
                console.log(img);
            })
        });
            // selector
            //     .append("option")
            //     .text(city)
            //     .property("value", city);
    
            // });
 
    });
}

// This function intialize the dashboard
function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#sel_city");

    // Use the list of sample names to populate the select options
    d3.json("/names").then((cities) => {
        //   console.log(cities);
        cities.forEach((city) => {
        selector
            .append("option")
            .text(city)
            .property("value", city);

        });

        const firstCity = cities[0];

        get_Cityfiles(firstCity);

    });

  // changeLayout();
}

// Initialize the dashboard
init();