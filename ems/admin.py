from django.contrib import admin

# Register your models here.

# Register Event model 
from .models import Event
admin.site.register(Event)

# Register Sponser model 
from .models import Sponsor
admin.site.register(Sponsor)

from .models import Category
admin.site.register(Category)

# Register News model 
from .models import News
admin.site.register(News)

from .models import Booking
admin.site.register(Booking)