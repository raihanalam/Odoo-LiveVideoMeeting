from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MeetingSchedule(models.Model):
    _name = 'meeting.schedule'
    _description = 'Meeting Schedule'
    _rec_name = 'meeting_header'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    meeting_header = fields.Char(string='Meeting Heading')
    image = fields.Binary(string='Image')
    meeting_date = fields.Date(string='Meeting Date')
    start_time = fields.Datetime(string='Start Time')
    end_time = fields.Datetime(string='End Time')
    meeting_host = fields.Many2one('res.users', string='Meeting Host', ondelete='cascade')
    participants = fields.Many2many('res.users', 'meeting_part_users', string='Meeting Participants', ondelete='cascade')
    meeting_type = fields.Selection(
        [
            ('private', 'private'),
            ('public', 'public'),
        ], default='private', string='Meeting Type'
    )

    def start_meeting(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': '/web#cids=1&default_active_id=mail.box_inbox&action=116&menu_id=84&active_id=mail.box_inbox'
        }
    def close_meeting(self):
        pass