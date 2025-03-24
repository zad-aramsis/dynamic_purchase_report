from odoo import api, models


class PurchaseOrderReport(models.AbstractModel):
    """Model for creating pdf report and data fetching """
    _name = 'report.purchase_report_generator.purchase_order_report'
    _description = "Purchase Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        """Function for get pdf report values"""
        if self.env.context.get('purchase_order_report'):
            if data.get('report_data'):
                data.update({'report_main_line_data': data.get('report_data')['report_lines'],
                             'Filters': data.get('report_data')['filters'],
                             'company': self.env.company})
            return data
