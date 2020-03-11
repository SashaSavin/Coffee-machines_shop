$.ajax({
    url : "http://localhost:8000/orders_list/order", 
    type : "POST", // http method
    data : { the_post : $('#post-text').val() },
    success : function(json) {
    $('#post-form').val(''); 
    console.log(json);
    console.log("success");
},

    error : function(xhr,errmsg,err) {
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
        " <a href='#' class='close'>&times;</a></div>"); 
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });