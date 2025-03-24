import json
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape


class TBXLSXReportController(http.Controller):
    """ This endpoint generates and provides an XLSX report in response to an
     HTTP POST request. The function uses the provided data to create the
     report and returns it as an XLSX file. """

    @http.route('/purchase_dynamic_xlsx_reports', type='http', auth='user', methods=['POST'], csrf=False)
    def get_report_xlsx(self, model, options, output_format, report_data, report_name, dfr_data, **kw):
        """Endpoint for getting xlsx report """
        uid = request.session.uid
        report_obj = request.env[model].with_user(uid)
        dfr_data = dfr_data
        options = options
        token = 'dummy-because-api-expects-one'
        try:
            if output_format == 'xlsx':
                response = request.make_response(None, headers=[('Content-Type', 'application/vnd.ms-excel'), ('Content-Disposition', content_disposition(report_name + '.xlsx'))])
                report_obj.get_purchase_xlsx_report(options, response, report_data, dfr_data)
            response.set_cookie('fileToken', token)
            return response
        except Exception as e:
            se = 0
            error = {
                'code': 200,
                'message': 'Odoo Server Error',
                'data': se
            }
            return request.make_response(html_escape(json.dumps(error)))
