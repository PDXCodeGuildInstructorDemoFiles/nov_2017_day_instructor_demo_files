// document.querySelector('#addToDo').addEventListener('click', function (e) {
//     e.preventDefault();
//     var in_value = document.getElementById('addToDoText').value;
//     console.log(in_value);
// });


$('#addToDo').click(function (e) {
    var input = $('#addToDoText');
    if (input.val().length > 0) {
        var new_task = $('<tr><td>' + input.val() + '</td><td><input type="checkbox" class="taskDone">' +
            '</td><td><a class="removeItem" href="#">x</a></td></tr>');
        var table = $('#toDoList');
        // table.append(new_task);
        new_task.hide().appendTo(table).fadeIn('slow');
        input.val('')
    }
});

// $('.tackDone').click(function (e) {
//     console.log('checkbox clicked')
// });

$('#toDoList')
    .on('change', '.taskDone', function (e) {
        if ($(this).prop('checked')) {
            $($(this).parent().prev()[0]).css('textDecoration', 'line-through')
        } else {
            $($(this).parent().prev()[0]).css('textDecoration', 'none')
        }
    })
    .on('click', '.removeItem', function (e) {
        e.preventDefault();
        $(this).parent().parent().fadeOut('slow', function () {
          $(this).remove()
        })
    });