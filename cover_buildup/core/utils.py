import csv
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import pandas as pd

from buildup.models import Unit, Reach


User = get_user_model()


def from_xlsx_to_csv_to_bd(author):
    data_xls = pd.read_excel('test_data.xlsx', 'Лист1', index_col='Unit')
    data_xls.to_csv('your_csv.csv', encoding='utf-8')
    tables = {}
    with open('your_csv.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if row[0] != 'Unit':
                tables[int(row[0])] = [float(val) for val in list(row[1:])]
                arg = Unit.objects.create(
                    unit=int(row[0]),
                    author=User.objects.get(id=author),
                )
                for val in list(row[1:]):
                    Reach.objects.create(
                        reach=val, unit=arg
                    )


def download_csv_to_xlsx(request):
    result = []
    unit_objects = Unit.objects.filter(author=request.user.id)
    for unit in unit_objects:
        reach_in_unit = Reach.objects.filter(
            unit=unit.id
        )
        result.append(
                [unit.unit, [reach.reach for reach in reach_in_unit]]
            )
    response = HttpResponse(content_type='text')
    writer = csv.writer(response)
    writer.writerow(
        ['Unit', 'Reach% 1+', 'Reach% 2+', 'Reach% 3+',
         'Reach% 4+', 'Reach% 5+', 'Reach% 6+', 'Reach% 7+',
         'Reach% 8+', 'Reach% 9+', 'Reach% 10+']
    )
    for val in result:
        writer.writerow([val[0], *val[1]])
    response['Content-Disposition'] = 'attachment; filename="somefilename.txt"'
    df = pd.read_csv("somefilename.txt")
    df.to_excel("data.xlsx", sheet_name="Testing", index=False)
    return response
