function generateList() {
    //Add list pulls
    for(i=0; i<list.size(); i++)
    {
        var add = "<li class='w3-bar'>" + 
        "<img src=" + list[i]['avatar'] + "class='w3-bar-item w3-circle w3-hide-small' style='width:85px'>" +
        "<div class='w3-bar-item'>" + 
        "    <span class='w3-large'>" + list[i]['Name'] + "</span><br>" +
        "    <span>"+ list[i]['Constituency'] + "</span>"  +
        "</div>" +
        "</li>";
        document.appendChild(add);
    }
}