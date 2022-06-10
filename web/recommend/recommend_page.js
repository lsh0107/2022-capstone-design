var movies = new Array();

d3.csv("movies.csv").then(function(data) {
    for (var i=0; i<data.length; i++){
        movies[i] = data[i]['title'];
    }
});

d3.csv("movies.csv").then(function(data) {
    console.log("Toy Story (1995)" == data[0]['title']);
});