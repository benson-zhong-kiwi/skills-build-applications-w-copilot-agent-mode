from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        self.stdout.write(self.style.WARNING('Deleting existing data...'))
        octo_models.User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create teams
        marvel = octo_models.Team.objects.create(name='Team Marvel')
        dc = octo_models.Team.objects.create(name='Team DC')

        # Create users
        users = [
            octo_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            octo_models.User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            octo_models.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            octo_models.User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            octo_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            octo_models.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        for user in users:
            octo_models.Activity.objects.create(user=user, type='Running', duration=30, calories=300)
            octo_models.Activity.objects.create(user=user, type='Cycling', duration=45, calories=400)

        # Create workouts
        for user in users:
            octo_models.Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session', duration=40)

        # Create leaderboard
        for team in [marvel, dc]:
            octo_models.Leaderboard.objects.create(team=team, points=1000)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
