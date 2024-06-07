from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Booking
from .models import Car

admin.site.register(Post)
admin.site.register(Booking)
admin.site.register(Car)