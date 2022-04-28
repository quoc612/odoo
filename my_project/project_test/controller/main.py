import json

import odoo

import logging

_logger = logging.getLogger(__name__)


class MyProjectAPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foo_handler(self):
        return "Hello"

    @odoo.http.route('/bar', auth='public')
    def bar_handler(self):
        return json.dumps({
            "content": "Welcome to 'bar' API"
        })

    @odoo.http.route(['/project/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def project_handler(self, dbname, id, **kwargs):
        model_name = "my.project"
        try:
            registry = odoo.modules.registry.Registry(dbname)
            with odoo.api.Environment.manage(), registry.cursor() as cr:
                env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
                rec = env[model_name].search([('id', '=', int(id))], limit=1)
                response = {
                    "status": "ok",
                    "content": {
                        "name": rec.name,
                        "age": rec.age,
                        "weight": rec.weight,

                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)
