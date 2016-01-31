$(document).ready(function () {
    'use strict';
    console.log('We Are Ready');

    function add_organization(target_form){
        var frm = $(target_form);
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                frm.find('.organization-add-form__btn-add').hide();
                frm.find('.organization-add-form__btn-close').show();
            },
            error: function(data) {
                console.log(data);
            }
        });
    }

    $('.organization-add-form').on('submit', function (event) {
        event.preventDefault();
        console.log('form submit routine');
        add_organization(event.target);
    });

});