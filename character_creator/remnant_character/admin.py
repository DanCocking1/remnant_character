from django.contrib import admin
from .models import User, Character, Weapon, DustPouch, PrimaryStatistics, Skills
admin.site.register(User)
admin.site.register(Character)
admin.site.register(Weapon)
admin.site.register(DustPouch)
admin.site.register(PrimaryStatistics)
admin.site.register(Skills)
# Register your models here.
