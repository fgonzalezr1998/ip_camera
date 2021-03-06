'use strict'

let login_info = {
    user: null,
    psswd: null,
}

function on_success(result) {
    if (result == "SUCCESS") {
        window.open("http://localhost:8888/", "_self");
    }
}

function credentials_ok(login_info) {
    // IMPLEMENT THIS TO TAKE CARE OF SQL INJECTION!
    return true;
}

function form_but_cb() {
    let x = $('form').serializeArray();
    $.each(x, function(i, field) {
        if (field.name == "user") {
            login_info.user = field.value;
        } else {
            login_info.psswd = field.value;
        }
    });

    if (!credentials_ok(login_info)) {
        console.log("Print a tooltip")
        return
    }

    // Check if user is authorized
    $.ajax({
      url: 'http://localhost:8888/login_check',
      type: 'GET',
      crossDomain: true,
      data: login_info,
      dataType: 'json',
      success: on_success,
      error: function(error) {
        alert("Error")
      }
    });
}

function main() {
    $('#form-but').click(form_but_cb);
}

$(document).ready(main)