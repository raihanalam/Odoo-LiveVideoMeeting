/** @odoo-module **/
import { onClickStartAMeetingButton } from '@mail/static/src/models/discuss'

//Custom function
odoo.define('test.live_meeting', function (require) {
    "use strict";
    var rpc = require('web.rpc');

    $(document).on('click', '#test_button', function(){
         console.log("test")
     });
});