from django.core.management.commands.startapp import Command as StartAppCommand


class Command(StartAppCommand):
    help = 'Creates a Django app with a custom template.'

    MODERN_APP_TEMPLATE = 'https://github.com/ilyachch-templates/django_application/archive/refs/heads/main.zip'

    def handle(self, **options):
        if not options.get('template', None):
            options['template'] = self.MODERN_APP_TEMPLATE
        super().handle(**options)
