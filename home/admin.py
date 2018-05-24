from django.contrib import admin
from .models import *


class CollegeModelAdmin(admin.ModelAdmin):
    list_display = ["c_name", "c_locality"]
    class Meta:
        model = College

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user", "mains_rank", "advanced_rank"]
    list_display_links = ["mains_rank"]
    list_filter = ["mains_rank"]
    search_fields = ["user__name", "mains_rank", "advanced_rank"]
    class Meta:
        model = Profile

admin.site.register(College, CollegeModelAdmin)
admin.site.register(Department)
admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(User)
