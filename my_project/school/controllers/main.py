import odoo, logging, json

_logger = logging.getLogger(__name__)


class MySchoolAPI(odoo.http.Controller):
    @odoo.http.route('/foo', auth='public')
    def foo_handler(self):
        return "Welcome to 'foo' API!"

    @odoo.http.route(['/school/<dbname>/<id>'], type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def school_handler(self, dbname, id, **kw):
        model_name = "student.student"
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
                        "gender": rec.gender,
                        "student_dob": rec.student_dob.strftime('%d/%m/%Y'),
                        "student_blood_group": rec.student_blood_group,
                        "nationality": rec.country,
                        # "weight": rec.weight,
                    }
                }
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)
