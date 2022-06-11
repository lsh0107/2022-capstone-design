function getValueInput(){
    var movies = []
    var inputValue = document.getElementById("userInput").value;
    d3.csv("movies.csv").then(function(data) {
        for (var i=0; i<data.length; i++){
            var title = data[i]['title'];
            if (title.toUpperCase().replace(" ","").indexOf(inputValue.toUpperCase().replace(" ","")) != -1) {
                movies.push(title);
            }
        }
    });
    console.log(movies);
}