var xhttp = new XMLHttpRequest();
xhttp.open("GET", "https://newsapi.org/v2/everything?q=bitcoin&apiKey=2df6c5b6bde4463996885f93d8998de4", true);
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       var data = xhttp.responseText;
       var out = JSON.parse(data);
       for(var i=0;i<out.articles.length;i++){
        document.getElementById("lst").innerHTML += '<div class="blog-card"><div class="meta"><div class="photo"><img src='
        +out.articles[i].urlToImage+
        '/></div><ul class="details"><li class="author"><a href="#">'
        +out.articles[i].author+
        '</a></li><li class="date">Aug. 24, 2015</li></ul></div><div class="description"><h1 class="title">'
        +out.articles[i].title+
        '</h1><h2>Updated: Nov 16, 2022, 17:07 IST</h2><p class="read-more"><a href="'
        +out.articles[i].url+
        '">Read More</a></p></div></div>';
        // style="background-image: url(https://static.toiimg.com/thumb/msid-95557833,imgsize-797716,width-400,resizemode-4/95557833.jpg)"
       }
    }
};
xhttp.send();