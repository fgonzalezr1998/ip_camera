'use strict'

export function user_authorized(login_info) {
    let Url = "http://127.0.0.1:8888/login_check/";

    $.ajax({
        url: Url,
        type: "GET",
        success: function(result) {
            console.log(result)
        },
        error: function(error) {
            console.log(error)
        }
    })

    /* $.get(url, login_info, function(data) {
        console.log(data)
    }); */
    return true;
}