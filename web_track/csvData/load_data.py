
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test_Drive_Google.settings")
import django

django.setup()

import csv

from web_track.models import Users, Trips, Events, Role

def load_roles():

    with open('/Users/shashank/PycharmProjects/Test_Drive_Google/web_track/csvData/roles.csv') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        Role.objects.bulk_create([Role(name= row[0]) for row in reader])
    print "Role data added"

def load_users():
    with open('/Users/shashank/PycharmProjects/Test_Drive_Google/web_track/csvData/users.csv') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        Users.objects.bulk_create([Users(user_id = row[0], company_id=row[1], email=row[2],
                                         role = Role.objects.get(id=row[3])) for row in reader])
    print "User data added"

def load_trips():
    with open('/Users/shashank/PycharmProjects/Test_Drive_Google/web_track/csvData/trips.csv') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        Trips.objects.bulk_create([Trips(trip_id = row[0], start_time = row[1], start_time_local = row[2], end_time = row[3],
                                         end_time_local = row[4], duration = row[5], distance = row[6],
                                         user_id = Users.objects.get(user_id=str(row[7])), score = row[8]) for row in reader])
    print "Trip data added"

def load_events():
    with open('/Users/shashank/PycharmProjects/Test_Drive_Google/web_track/csvData/events.csv') as f:
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        Events.objects.bulk_create([Events(event_id=row[0], trip_id=Trips.objects.get(trip_id=str(row[1])),
                                           event_type=row[2], event_ts=row[3], event_ts_local=row[4],
                                           geo_lat=row[5], geo_long=row[6], altitude=row[7], vert_accuracy=row[8],
                                           horiz_accuracy=row[9], heading=row[10], speed = row[11]) for row in reader])
    print "Event data added"

load_roles()
load_users()
load_trips()
load_events()