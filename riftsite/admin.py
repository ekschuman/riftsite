from django.contrib import admin
from models import Faction, FactionRank, FactionRegistration, Divine, Character, Item, ItemOwned

# Register your models here.

admin.site.register(Faction)
admin.site.register(FactionRank)
admin.site.register(FactionRegistration)
admin.site.register(Divine)
admin.site.register(Character)
admin.site.register(Item)
admin.site.register(ItemOwned)