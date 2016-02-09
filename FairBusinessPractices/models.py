# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Office(models.Model):
    office_id = models.IntegerField(primary_key=True)
    office_desc = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_code = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.office_id) + " - " + self.office_desc

    class Meta:
        managed = False
        db_table = 'offices'


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    violation = models.ForeignKey('Violation', models.DO_NOTHING)
    office = models.ForeignKey(Office, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.CharField(max_length=1)
    created_ts = models.DateTimeField()
    updated_ts = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

    class Meta:
        managed = False
        db_table = 'patients'


class Violation(models.Model):
    violation_id = models.IntegerField(primary_key=True)
    violation_desc = models.CharField(max_length=100)

    def __str__(self):
        return str(self.violation_id) + " - " + self.violation_desc

    class Meta:
        managed = False
        db_table = 'violations'
