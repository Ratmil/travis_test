from openerp.osv import fields, osv


class travis_test(osv.osv):

    _name = "travis.test"
    _description = "Travis Test"

    _columns = {
        'name': fields.char('Name', size=150, select=True),
    }
