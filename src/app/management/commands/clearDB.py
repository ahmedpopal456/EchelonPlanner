from app.subsystem.database.coursecatalog import *
import json
import logging
import django.core.exceptions

from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Delete DB course contents'

    def handle(self, *args, **options):

        Course.objects.all().delete()
        Event.objects.all().delete()