from django.contrib import admin
from .models import User, listing, bid, comment, close_listing, watch_list

# Register your models here.

admin.site.register(User)
admin.site.register(listing)
admin.site.register(bid)
admin.site.register(comment)
admin.site.register(close_listing)
admin.site.register(watch_list)




