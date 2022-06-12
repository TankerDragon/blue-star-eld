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
YEARS = (
    ('99', '1999'),
    ('00', '2000'),
    ('01', '2001'),
    ('02', '2002'),
    ('03', '2003'),
    ('04', '2004'),
    ('05', '2005'),
    ('06', '2006'),
    ('07', '2007'),
    ('08', '2008'),
    ('09', '2009'),
    ('10', '2010'),
    ('11', '2011'),
    ('12', '2012'),
    ('13', '2013'),
    ('14', '2014'),
    ('15', '2015'),
    ('16', '2016'),
    ('17', '2017'),
    ('18', '2018'),
    ('19', '2019'),
    ('20', '2020'),
    ('21', '2021'),
    ('22', '2022'),
    ('23', '2023'),
)
FUEL_TYPE = (
    ('di', 'Diesel'),
    ('ga', 'Gasoline'),
    ('pr', 'Propane'),
    ('li', 'Liquid Natural Gas'),
    ('co', 'Compressed Natural Gas'),
    ('me', 'Methanol'),
    ('e', 'E-85'),
    ('m', 'M-85'),
    ('a', 'A55'),
    ('bi', 'Biodisel'),
    ('o', 'Other'),
)
# Create your models here.
class Vehicle(models.Model):
    unit_number = models.CharField(max_length=10, unique=True)
    make = models.CharField(max_length=15, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=2, choices=YEARS, default='22')
    license_state = models.CharField(max_length=2, choices=STATES, default='NY')
    license_number = models.CharField(max_length=20, null=True)
    vin_number = models.CharField(max_length=20, blank=True, null=True)
    fuel_type = models.CharField(max_length=2, choices=FUEL_TYPE, default='di')
    eld_device = models.CharField(max_length=16, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.unit_number


class Driver(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cdl_number = models.CharField(max_length=20, unique=True)
    cdl_state = models.CharField(max_length=2, choices=STATES, default='NY')
    vehicle = models.OneToOneField(Vehicle, blank=True, null=True, on_delete=models.SET_NULL)
    co_driver = models.OneToOneField('self', blank=True, null=True, on_delete=models.SET_NULL)
    company_user_id = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length = 10, blank=True, null=True)
    app_version = models.CharField(max_length=5, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


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