from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faction(models.Model):
    def __unicode__(self):
        return 'Faction: ' + self.name
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, default="")

class FactionRank(models.Model):
    def __unicode__(self):
        return 'Faction: ' + self.faction.name + ' Rank: ' + self.name
    name = models.CharField(max_length=200)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='ranks')
    rank_level = models.IntegerField(default=0)

class Divine(models.Model):
    def __unicode__(self):
        return 'Divine: ' + self.name
    name = models.CharField(max_length=200)
    favor = models.CharField(max_length=1000)

class Character(models.Model):
    def __unicode__(self):
        if self.player == 1:
            prefix = "Player"
        else:
            prefix = "Non-Player"
        return prefix + ' Character: ' + self.name
    user = models.ForeignKey(User, blank=True, null=True, related_name='characters')

    name = models.CharField(max_length=200)
    player = models.IntegerField(default=0)
    patron_divine = models.ForeignKey(Divine, models.SET_NULL, blank=True, null=True, related_name='followers')
    race = models.CharField(max_length=200, default='Human')
    subrace = models.CharField(max_length=200, blank=True, null=True)

    lives = models.IntegerField(default=7)
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    hit_points = models.IntegerField(default=2)
    max_mana = models.IntegerField(default=4)
    vitality = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    endurance = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    faith = models.IntegerField(default=1)
    discipline = models.IntegerField(default=1)
    points_to_spend = models.IntegerField(default=5)
    silver = models.IntegerField(default=0)

class FactionRegistration(models.Model):
    def __unicode__(self):
        return 'Registration: ' + self.character.name + " In " + self.faction.name + " As " + self.faction_rank.name
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='registration')
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='registration')
    faction_rank = models.ForeignKey(FactionRank, on_delete=models.CASCADE, related_name='registration')

class Item(models.Model):
    def __unicode__(self):
        return 'Item: ' + self.name
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class ItemOwned(models.Model):
    def __unicode__(self):
        return 'Ownership: ' + self.owner.name + " owns " + self.item.name
    owner = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='item_owned')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_owned')
    count = models.IntegerField(default=1)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)