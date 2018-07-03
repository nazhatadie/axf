# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Comments(models.Model):
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='id', primary_key=True)
    mov = models.ForeignKey('Movie', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class Event(models.Model):
    click_counts = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'event'


class Movie(models.Model):
    id = models.ForeignKey(Event, models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=64)
    img = models.CharField(max_length=128)
    des = models.CharField(max_length=256)
    area = models.CharField(max_length=128)
    actors = models.CharField(max_length=128)
    year = models.CharField(max_length=16)
    score = models.FloatField()
    status = models.IntegerField()
    url = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'movie'


class MovieTypename(models.Model):
    movie = models.ForeignKey('MovieTypes', models.DO_NOTHING, primary_key=True)
    id = models.ForeignKey(Movie, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'movie_typename'
        unique_together = (('movie', 'id'),)


class MovieTypes(models.Model):
    type_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_types'


class Nav(models.Model):
    huge_pic = models.CharField(max_length=128)
    small_pic = models.CharField(max_length=128)
    movie_name = models.CharField(max_length=10, blank=True, null=True)
    movie_desc = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nav'


class Permission(models.Model):
    id = models.ForeignKey('User', models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'permission'


class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=11)
    user_formail = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'user'


class UserStatus(models.Model):
    id = models.ForeignKey(User, models.DO_NOTHING, db_column='id', primary_key=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_status'
