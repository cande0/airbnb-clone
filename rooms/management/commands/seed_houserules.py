from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates House rules!"

    def handle(self, *args, **options):
        houserules = [
            "Suitable for events",
            "Pets allowed",
            "Smoking allowed",
        ]
        for h in houserules:
            HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS(f"{len(houserules)} House Rules Created!"))
