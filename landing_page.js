function validate()
{
    var uid = document.getElementById('inp').value;
    window.localStorage.setItem('User',uid);
    req = {usr:uid}
    $.ajax({
        type : 'POST',
        url : 'dummyurl.com',
        data : JSON.stringify(req),
        contentType : "application/json",
        success : function(data)    {
            console.log(data);
            window.location.replace('voting.html')
        },
        error : function()  {
            window.location.reload();
            alert("Error loading credentials. Please try again.");
        } 
    });
}