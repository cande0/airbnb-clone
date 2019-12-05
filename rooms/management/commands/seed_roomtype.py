from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates Room Types!"

    def handle(self, *args, **options):
        roomtypes = [
            "Entire lace",
            "Private room",
            "Hotel room",
            "Shared room",
        ]
        for r in roomtypes:
            RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(roomtypes)} Room Types Created!"))
