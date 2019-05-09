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
    list = ["categories", "word", "topstore", "leaststore", "review", "rating"];
    // d3.select("#word").attr("src", "static/img/entrepreneur_logo.jpg");
    // imglist = d3.select("img");
    // console.log(imglist);

    // alert(name);
    url = "/select/" + name
    d3.json(url).then(function(results) {
        // console.log(results);
        // Loop thru jsonify object list, find match, & write image path
        Object.entries(results).forEach(([id, item]) => {
            // console.log(id);
            item.forEach(img => {
                for (var i = 0; i < list.length; i++) {
                    // Check if img path string contain item in list
                    // If so, write image path to item list id
                    imgString = img.toString().toLowerCase();
                    idString = String(list[i]);
                    // console.log(imgString.search(idString));
                    if (imgString.search(idString) > 0) {
                        image = document.getElementById(list[i]);
                        image.src = img;
                        // console.log(img);
                        // console.log(list[i]);
                    }else{
                        if (imgString.search("my_map") > 0) {
                            image = document.getElementById("my_map");
                            image.href = img;
                        }
                    }
                }
            })
        });
 
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