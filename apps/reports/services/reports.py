from apps.reports import models
from apps.users.models import User


class BaseReportService:
    def fill_reports(self, reps_list: list[dict], reps_columns: dict[str, list]):
        for rep in reps_list:
            for key, value in rep.items():
                if key in reps_columns:
                    reps_columns[key].append(value)
        return reps_columns


class DailyReportService(BaseReportService):
    def make_columns_dict(self):
        return {
            'id': [],
            'serial_number': [],
            'date': [],
            'agent_id': [],
            'supplier_id': [],
            'agent_sum': [],
            'supplier_sum': [],
            'direction': [],
            'comment': [],
            'marja': [],
            'user_id': []
        }

    def collect_reports(self, reports):
        columns = self.make_columns_dict()
        reps = []
        for rep in reports:
            rep2 = rep.copy()
            rep2['agent_id'] = models.Agent.objects.get(pk=rep['agent_id']).name
            rep2['supplier_id'] = models.Supplier.objects.get(pk=rep['supplier_id']).name
            rep2['user_id'] = User.objects.get(pk=rep['user_id']).username
            reps.append(rep2)

        return self.fill_reports(reps, columns)


class CommonReportService(BaseReportService):
    def make_columns_dict(self):
        return {
            "serial_number": [],
            "date": [],
            "agent_sum": [],
            "direction": [],
            "agent_payment": [],
            "balance": [],
            "comment": [],
            "user": []
        }

    def collect_reports(self, reports):
        columns = self.make_columns_dict()
        reps = []
        for rep in reports:
            rep_copy = rep.copy()
            rep_copy['user_id'] = User.objects.get(pk=rep['user_id']).username
            reps.append(rep_copy)
        return self.fill_reports(reps, columns)


rows = [
    'id',
    'номер',
    'дата',
    'агент',
    'поставщик',
    'сумма агент',
    'сумма поставщик',
    'направление',
    'комментарий',
    'маржа'
]
