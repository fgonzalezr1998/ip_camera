'use strict'

export function user_authorized(login_info) {
    let Url = 'http://localhost:8888/login_check';

    $.ajax({
        url: Url,
        type: 'POST',
        data: login_info,
        dataType: 'json',
        success: function(result) {
            alert("ok")
        },
        error: function(error) {
            alert("Error")
        }
    });

    /* $.get(Url, login_info, function(data) {
        console.log(data)
    }); */
    return true;
}