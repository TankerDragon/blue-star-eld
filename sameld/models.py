from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('OFF', 'Off duty'),
    ('SB', 'Sleeper berth'), 
    ('DR', 'Driving'), 
    ('ON', 'On duty'), 
    ('YM', 'Yard moves'),
    ('PC', 'Personal conveyance')
]
STATES = [
    ("AK", "Alaska"), 
    ("AL", "Alabama"), 
    ("AR", "Arkansas"), 
    ("AS", "American Samoa"), 
    ("AZ", "Arizona"), 
    ("CA", "California"), 
    ("CO", "Colorado"), 
    ("CT", "Connecticut"), 
    ("DC", "District of Columbia"), 
    ("DE", "Delaware"), 
    ("FL", "Florida"), 
    ("GA", "Georgia"), 
    ("GU", "Guam"), 
    ("HI", "Hawaii"), 
    ("IA", "Iowa"), 
    ("ID", "Idaho"), 
    ("IL", "Illinois"), 
    ("IN", "Indiana"), 
    ("KS", "Kansas"), 
    ("KY", "Kentucky"), 
    ("LA", "Louisiana"), 
    ("MA", "Massachusetts"), 
    ("MD", "Maryland"), 
    ("ME", "Maine"), 
    ("MI", "Michigan"), 
    ("MN", "Minnesota"), 
    ("MO", "Missouri"), 
    ("MS", "Mississippi"), 
    ("MT", "Montana"), 
    ("NC", "North Carolina"), 
    ("ND", "North Dakota"), 
    ("NE", "Nebraska"), 
    ("NH", "New Hampshire"), 
    ("NJ", "New Jersey"), 
    ("NM", "New Mexico"), 
    ("NV", "Nevada"), 
    ("NY", "New York"), 
    ("OH", "Ohio"), 
    ("OK", "Oklahoma"), 
    ("OR", "Oregon"), 
    ("PA", "Pennsylvania"), 
    ("PR", "Puerto Rico"), 
    ("RI", "Rhode Island"), 
    ("SC", "South Carolina"), 
    ("SD", "South Dakota"), 
    ("TN", "Tennessee"), 
    ("TX", "Texas"), 
    ("UT", "Utah"), 
    ("VA", "Virginia"), 
    ("VI", "Virgin Islands"), 
    ("VT", "Vermont"), 
    ("WA", "Washington"), 
    ("WI", "Wisconsin"), 
    ("WV", "West Virginia"), 
    ("WY", "Wyoming")
]
# Create your models here.
class Vehicle(models.Model):
    unit_number = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=20, null=True)
    vin_number = models.CharField(max_length=20, null=True)
    notes = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=1)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cdl_number = models.CharField(max_length=20, unique=True)
    cdl_state = models.CharField(max_length=2, choices=STATES, default='NY')
    vehicle = models.OneToOneField(Vehicle, blank=True, null=True, on_delete=models.SET_NULL)
    co_driver = models.OneToOneField('self', blank=True, null=True, on_delete=models.SET_NULL)
    company_user_id = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length = 10, blank=True, null=True)
    app_version = models.CharField(max_length=5, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=1)


class Log(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices= STATUS_CHOICES, default='OFF')
    date = models.DateField()
    time = models.TimeField()
    loc_name = models.CharField(max_length=50, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    odometer = models.IntegerField(null=True)
    eng_hours = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    notes = models.CharField(max_length=20, null=True)
    document = models.CharField(max_length=20, null=True)
    trailer = models.CharField(max_length=20, null=True)