//Отправление ajax запроса на сервер (шаблон валидации)

// $.ajax({
// 	type: "GET",
// 	url: "",
// 	data: {
// 		""
// 	}
// 	dataType: "text",
// 	cache: false,
// 	success: function (data) {
// 		console.log(data);
// 		if (data == 'ok') {
// 			$
// 		}
// 	}
// })


$.ajax({
    url: '127.0.0.1:8000/login',
    type: 'POST',
    success: function(data) {
        alert('ok!');
    },
    failure: function(data) { 
        alert('Got an error, dude');
    }
}); 