from django.core.management.base import BaseCommand
import os
import sys
import sqlite3
import csv
from report.models import Report


class Command(BaseCommand):
    help = 'Bulk load csv data to sql'

    def add_arguments(self, parser):
        parser.add_argument('data_file', type=str, help='New Django Project Name')

    def handle(self, *args, **kwargs):
        data_file = kwargs['data_file']

        with open(data_file, 'rt') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                report = Report.objects.create(
                    firstoccurrence=row['FIRSTOCCURRENCE'],
                    node=row['NODE'],
                    severity=row['ORIGINALSEVERITY'],
                    alarm=row['X733SPECIFICPROB']
                )
                report.save()

        self.stdout.write(self.style.SUCCESS('Bulk data inserted into Database from %s' % data_file))
