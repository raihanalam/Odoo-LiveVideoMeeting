//import { onClickStartAMeetingButton } from '@mail/static/src/models/discuss'
//Custom function
odoo.define('live_meeting.test', function (require) {
    "use strict";
    var rpc = require('web.rpc');
    var my_discuss = require('mail.discuss');

//    var meeting_model = require('web.mail');
//    var custom_models = meeting_model.Discuss.extend({
//        _created() {
//            super._created();
//            // Bind necessary until OWL supports arrow function in handlers: https://github.com/odoo/owl/issues/876
//            this.onClickStartAMeetingButton = this.onClickStartAMeetingButton.bind(this);
//        }
//    });
//    meeting_model.Discuss = custom_models;

    $(document).on('click', '#test_button', function(){
         console.log("test")
    });
});

