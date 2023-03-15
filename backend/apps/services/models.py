from datetime import timedelta
from django.db import models
from apps.auth.models import User 

class ServiceType(models.Model):
    name = models.CharField(max_length=155, unique=True)
    def __str__(self):
        return self.name
    @property
    def get_services(self):
        return self.service_set.all()
    

class Service(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=155, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title != None and self.title != '' else self.service_type.name + str(self.id) 
    
    @property
    def total_length(self):
        items = self.orderitem_set.all()
        total_seconds =  sum([item.length.total_seconds() for item in items])
        return timedelta(seconds=total_seconds)


class Team(models.Model):
    service = models.ManyToManyField(Service, blank=True, related_name="service_teams")
    name = models.CharField(max_length=155, blank=True, null=True)
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return "Equipo de %s" % (self.name)

class Role(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True);
    name = models.CharField(max_length=120, null=True, blank=True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return "%s - %a" % (self.team, self.name)
    
class ServiceOrderItem(models.Model):
    TYPE_OPTIONS = [
        ('a', 'Item'),
        ('b', 'Header'),
    ]
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service_order_items")
    item_type = models.CharField(max_length=1,
                            choices=TYPE_OPTIONS,
                            null=True, default='a')
    length = models.DurationField(blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    person = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.title