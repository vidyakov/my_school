from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'create my own superuser'

    def handle(self, *args, **kwargs):
        superuser = User(
            username='superuser',
            email='admin@admin.com',
            is_superuser=True,
            is_staff=True
        )
        superuser.set_password('qwerty')
        superuser.save()

