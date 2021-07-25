from django.contrib import admin
from .models import Meetup, Location, Participant, Quiz, Reply

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display=('title', 'slug')
    list_filter=('location', 'date_n_time', )
    prepopulated_fields={'slug':('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Quiz)
admin.site.register(Reply)