from odoo import models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    def action_open_general_ledger_wizard(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "General Ledger",
            "res_model": "general.ledger.report.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_account_ids": [self.default_account_id.id]
                if self.default_account_id
                else [],
            },
        }
