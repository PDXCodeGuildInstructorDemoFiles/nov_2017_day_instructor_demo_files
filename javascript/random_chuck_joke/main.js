function grab_joke() {
    $.ajax({
        url: 'http:/m',
        type: 'GET',
        success: function (response) {
            $('#jokeId').text(response.value.id);
            $('#v').text(response.value.joke);
        },
        error: function (e) {
            console.log(e)
        }

    });
}

$('#factMe').click(grab_joke);
grab_joke();