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

    //events
    $('.organization-add-form').on('submit', function (event) {
        event.preventDefault();
        console.log('form submit routine');
        add_organization(event.target);
    });

    $('.modal').on('hidden.bs.modal', function (e) {
        console.log('form closed');
        var formApproved = $('.organization-add-form__btn-add').css('display') == 'none';
        if (!formApproved) {
            return;
        }

        $(this)
            .find('input,textarea,select')
               .val('').end()
            .find('input[type=checkbox], input[type=radio]')
               .prop("checked", "").end()
            .find('.organization-add-form__btn-add')
                .show().end()
            .find('.organization-add-form__btn-close')
                .hide().end();
    })

});