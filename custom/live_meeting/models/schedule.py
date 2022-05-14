from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MeetingSchedule(models.Model):
    _name = 'meeting.schedule'
    _description = 'Meeting Schedule'
    _rec_name = 'meeting_header'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    meeting_header = fields.Char(string='Meeting Heading')
    meeting_date = fields.Date(string='Meeting Date')
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    meeting_host = fields.Many2one('res.users', string='Meeting Host')
    participants = fields.Many2many('res.users', string='Meeting Participants')
    meeting_type = fields.Selection(
        [
            ('private', 'private'),
            ('public', 'public'),
        ], default='private', string='Meeting Type'
    )

    def start_meeting(self):
        pass

    def close_meeting(self):
        pass