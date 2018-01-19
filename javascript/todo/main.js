$(document).on('change', '.strikeThrough', function () {
    if ($(this).prop('checked')) {
        $(this).parent().next().addClass('strike')
    } else {
        $(this).parent().next().removeClass('strike')
    }
});

$('#todoTable').on('click', '.remove', function (e) {
    e.preventDefault();
    $(this).parent().parent().remove();
});

$('#addTodo').click(function (e) {
    // console.log('click');
    var value = $('#newTask');
    // language=HTML
    $('#todoTable').append('<tr><td><input type="checkbox" class="strikeThrough"></td><td>' + value.val() + '</td><td><a href="#" class="remove">x</a> </td></tr>');
    value.val('')
});


