from django.contrib import admin
from education.models import Document, People


class DocRelation(admin.StackedInline):
    """ Extends StackedInline method

     enables to add education information to related field

     """
    model = Document
    extra = 0


class PeopleAdmin(admin.ModelAdmin):
    inlines = [DocRelation]

admin.site.register(People, PeopleAdmin)

