from django.contrib import admin

from cv.models import Profil, Competencie, Experience, Formation, Contact


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'first_name',
        'last_name',
        'description',
    )


@admin.register(Competencie)
class CompetencieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'percentage',
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'company',
        'date_start',
        'date_end',
        'description',
    )


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'date_start',
        'date_end',
        'description',
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'icon',
        'title',
    )


