from django.db import models
from django.contrib import auth
from django.utils import timezone


# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return self.username


class Character(models.Model):
    created_by = models.ForeignKey(User, related_name='player', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField(default=18)
    race = models.CharField(max_length=12)
    aura = models.CharField(max_length=64)
    sembelence = models.CharField(max_length=64)
    gender = models.CharField(max_length=10)
    fanuas_type = models.CharField(max_length=32)
    citizenship = models.CharField(max_length=32)
    occupation = models.CharField(max_length=32)
    background = models.TextField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.surname + ", " + self.first_name


class Weapon(models.Model):
    # player = models.ForeignKey(User,related_name='player_name', on_delete=models.CASCADE)
    wielder = models.ForeignKey(Character, related_name='PC', on_delete=models.CASCADE)
    weapon_name = models.CharField(max_length=128)
    weapon_type = models.CharField(max_length=64)
    wield_type = models.CharField(max_length=7)
    attack_speed = models.CharField(max_length=16)
    hit_bonus = models.PositiveSmallIntegerField()
    damage_class = models.CharField(max_length=32)
    damage_bonus = models.SmallIntegerField()
    weapon_range = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.weapon_name


class PrimaryStatistics(models.Model):
    character_name = models.ForeignKey(Character, related_name='player_stats', on_delete=models.CASCADE)
    strength = models.PositiveSmallIntegerField(default=10)
    dexterity = models.PositiveSmallIntegerField(default=10)
    constitution = models.PositiveSmallIntegerField(default=10)
    charisma = models.PositiveSmallIntegerField(default=10)
    intelligence = models.PositiveSmallIntegerField(default=10)
    wisdom = models.PositiveSmallIntegerField(default=10)
    armor_rating = models.PositiveSmallIntegerField(default=10)
    player_level = models.PositiveSmallIntegerField(default=1)
    hit_points = models.PositiveIntegerField(default=10)
    exp = models.PositiveIntegerField(default=0)


class DustPouch(models.Model):
    character_owner = models.ForeignKey(Character, related_name='character_dust', on_delete=models.CASCADE)
    wind = models.PositiveSmallIntegerField(default=0)
    fire = models.PositiveSmallIntegerField(default=0)
    lightning = models.PositiveSmallIntegerField(default=0)
    water = models.PositiveSmallIntegerField(default=0)


class Skills(models.Model):
    character_skilled = models.ForeignKey(Character, related_name='char_skills', on_delete=models.CASCADE)
    acrobatics = models.PositiveSmallIntegerField(default=0)
    animal_handling = models.PositiveSmallIntegerField(default=0)
    dust = models.PositiveSmallIntegerField(default=0)  # from arcana, makes more sense in remnant, even with maidens
    athletics = models.PositiveSmallIntegerField(default=0)
    deception = models.PositiveSmallIntegerField(default=0)
    history = models.PositiveSmallIntegerField(default=0)
    insight = models.PositiveSmallIntegerField(default=0)
    intimidation = models.PositiveSmallIntegerField(default=0)
    investigation = models.PositiveSmallIntegerField(default=0)
    medicine = models.PositiveSmallIntegerField(default=0)  # aura?
    nature = models.PositiveSmallIntegerField(default=0)
    perception = models.PositiveSmallIntegerField(default=0)
    performance = models.PositiveSmallIntegerField(default=0)
    grimm = models.PositiveSmallIntegerField(default=0)
    sleight_of_hand = models.PositiveSmallIntegerField(default=0)
    stealth = models.PositiveSmallIntegerField(default=0)
    survival = models.PositiveSmallIntegerField(default=0)
