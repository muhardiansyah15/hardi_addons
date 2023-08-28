odoo.define( 'user_terms_acceptance.popup_tnc_acceptance', function (require) {
    'use strict';
    var ajax = require('web.ajax');
    $(document).ready(function () {
        // Show the modal on page load
        $('#TcModal').modal('show');
    });

    // Handle the "I Agree" button click event
    $('#agreeButton').click(function () {
        window.location.href = '/accepted_terms';
    });
});
