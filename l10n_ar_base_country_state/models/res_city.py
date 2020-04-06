##############################################################################
#   Copyright (c) 2018 Eynes/E-MIPS (www.eynes.com.ar)
#   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
##############################################################################

from odoo import models, fields, api


class ResCity(models.Model):
    _name = 'res.city'
    _description = 'Cities'

    @api.multi
    def name_get(self):
        ret = []
        for city in self:
            if city.state_id:
                ret.append((city.id, "[%s] %s (%s)" % (city.zip_code or '', city.name,
                                                  city.state_id.name or '')))
            else:
                ret.append((city.id, city.name))

        return ret

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if len(args) == 1 and args[0][0] == 'name':
            name = args[0][2]
            args = [
                '|',
                ['zip_code', '=ilike', name + '%'],
                ['name', 'ilike', name]
            ]
        res = super()._search(
            args=args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
        return res

    @api.onchange("state_id")
    def onchange_state_id(self):
        if self.state_id and self.country_id != self.state_id.country_id:
            self.country_id = self.state_id.country_id and \
                self.state_id.country_id.id

    def default_country_id(self):
        return self.env.ref("base.ar").id

    name = fields.Char(string='City', size=64, required=True)
    zip_code = fields.Char(string='Zip', size=24)
    afip_code = fields.Char(string='AFIP Code', size=16)
    country_id = fields.Many2one(
        'res.country', string='Country', default=default_country_id)
    state_id = fields.Many2one('res.country.state', string='Country State')
