from pickletools import TAKEN_FROM_ARGUMENT1
from django.contrib import admin
from apps.services.models import *

admin.site.register([
    ServiceType,
    Service,
    ServiceOrderItem,
    Team,
    Role,
])
