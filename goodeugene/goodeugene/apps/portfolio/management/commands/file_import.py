from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from apps.portfolio.file_import import excelImport

class Command(BaseCommand):
    help='''Import excelfile'''
    option_list = BaseCommand.option_list + (
        make_option('--excel',
            help='tells you what file'),
        )
   
    def handle(self, **options):
        excelImport(options['excel'])
