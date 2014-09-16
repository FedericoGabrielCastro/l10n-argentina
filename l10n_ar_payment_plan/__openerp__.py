# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Aconcagua Team (http://www.proyectoaconcagua.com.ar)
#    All Rights Reserved. See AUTHORS for details.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Planificacion de Pagos",
    "version": "1.0",
    "depends": ["base", "purchase", "account" , "account_accountant", "account_payment" ],
    "author": "Aconcagua Team",
    "website": "http://www.proyectoaconcagua.com.ar",
    "license": "GPL-3",
    "category": "",
    "description": """
      Modulo de planificacion de pagos con posibilidad de crear de forma semi automatica los vouchers a partir de la planificacion realizada.
    """,
    "data": [
    ],
    'demo': [
        ],
    'test': [
    ],
    'installable': True,
    'active': False,
}
