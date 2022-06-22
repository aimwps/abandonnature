from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from verfications.models import Verfication


class Verification(models.Model):
    VERIFICATION_TYPES = (("basic_web", "Basic web"), ("local_web", "Local web"), ("eye_witness", "Eye witness"))
    type = models.CharField(max_length=100, choices=VERIFICATION_TYPES)
    is_postive = models.BooleanField()
    content_type =  models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

class Reaction(models.Model):
    REACTION_TYPES = (("peace", "peace"), ("love", "love"), ("shock", "shock"), ("laugh", "laugh"), ("joy", "joy"))

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type =  models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    body = models.TextField(max_length=500)
    reactions = GenericRelation(Reaction)

class NatureStatus(models.Model):
    STATUS_TYPES = (("abandoned", "abandoned"), ("occupied", "occupied"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_TYPES)
    message = models.TextField(blank=True, null=True)
    access_note = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    verifications = GenericRelation(Verifications)
    loc_lat = models.FloatField(blank=True, null=True)
    loc_lon = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="evidence")
    comments = GenericRelation(Comment)

class CleanUp(models.Model):
    STATUS_TYPES = (("scheduled", "scheduled"), ("complete", "complete"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_TYPES)
    message = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    verifications = GenericRelation(Verifications)
    comments = GenericRelation(Comment)

class CleanUpContributor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    cleanup = models.ForeignKey(CleanUp, on_delete = models.CASCADE, related_name="contributors")
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class CleanUpTags(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(NatureStatus, on_delete=models.CASCADE, related_name="cleanups")
    on_cleanup = models.ForeignKey(CleanUp, on_delete=models.CASCADE, related_name="tags")



    # def basic_web_votes()
