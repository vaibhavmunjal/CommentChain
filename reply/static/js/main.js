$(function(){
    $("#comment-list").on("click", ".reply", function(e){
        e.preventDefault();
        let form = $("#comment-form").clone(true);
        if ($(this).parent().find('#comment-form').length !== 0){}
        else {
        form.find('.parent').val($(this).parent().parent().attr('id'));
        $(this).parent().append(form);
        }
    });

    $("#comment-list").on("click", ".delete", function(e) {
        e.preventDefault();
        const id = $(this).attr('data-path');
        console.log(id);

        $.ajax({
            type: 'POST',
            url: 'delete',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                id: id
            },
            success: function(result) {
                if (result.deleted) {
                    console.log("got deleted");
                    window.location = '';
                }
            }
        });
    });



});
