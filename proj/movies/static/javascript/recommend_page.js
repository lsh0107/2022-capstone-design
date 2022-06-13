//
//function getValueInput(){
//    const element = document.getElementById('searchResult');
//    element.innerHTML = '검색 결과';
//    var movies = []
//    var inputValue = document.getElementById("userInput").value;
//    $(function() {
//        var fileName = "C:/Users/admin/Desktop/movies.csv";
//        var movies = [];
//        $.ajax({
//            url:fileName,
//            dataType:'text',
//            success: function(data) {
//                var allRow = data;
//                //.split(/\r?\n|\r/)
//                var textLine = '';
//                index = data.indexOf('\n') + 1;
//                for (var i=index; i<data.length; i++){
//                    startIndex = data.indexOf(',', i)+1;
//                    endIndex = data.indexOf(',', startIndex+1);
//                    end_lineIndex = data.indexOf('\n', endIndex+1);
//                    i = end_lineIndex+1;
//                    secondData = data.slice(startIndex, endIndex);
//                    movies.push(secondData);
//                }
//                // $('#searchResult').append("<br>");
//                // $('#searchResult').append(textLine);
//                movieList = [];
//                for (var i=0; i<movies.length; i++){
//                    var title = movies[i];
//                    if (title.toUpperCase().replace(" ","").indexOf(inputValue.toUpperCase().replace(" ","")) != -1) {
//                        movieList.push(title);
//                    }
//                }
//                $('#searchResult').append("<hr>");
//
//                for (var i=0; i<movieList.length; i++){
//                    var textLine = movieList[i];
//                    $('#searchResult').append("<div id="+i+" onclick=\"dataSave(this.id)\">"+textLine+"</div>");
//                }
//            }
//        }
//        );
//    }
//    );
//
//}
//
//// 여기 data에 user가 검색해서 선택한 영화 제목이 담겨있음.
//function dataSave(clickedID){
//    var data = document.getElementById(clickedID).innerText;
//    console.log(data);
//    return data;
//}