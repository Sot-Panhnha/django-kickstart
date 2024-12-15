import sys
from django.core.management.base import CommandError
from django.core.management.commands.migrate import Command as MigrateCommand


class Command(MigrateCommand):
    help = 'Migrate all apps in the inventory database'

    def handle(self, *args, **options):
        app_label = options.get('app_label')

        if not app_label:
            raise CommandError('The migrate command does not accept a specific app_label argument')
        
        if '--database' not in sys.argv:
            raise CommandError('The migrate command must include a --database argument')
        
        super().handle(*args, **options)
            

# Path: inventory/management/commands/migrate.py to create a custom management command called migrate.py
# Example: python manage.py migrate --database inventory_db inventory