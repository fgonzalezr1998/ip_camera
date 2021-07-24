'use strict'

import * as db from './db_utils.js';

let login_info = {
    user: null,
    psswd: null,
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

    if (db.user_authorized(login_info)) {
        window.open("test.html", "_self");
    }
}

function main() {
    $('#form-but').click(form_but_cb);
}

$(document).ready(main)