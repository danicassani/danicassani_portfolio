from collections.abc import Iterable
from typing import Any
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    date = models.DateField()

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    order = models.AutoField(primary_key=True)

class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateField(null=True, blank=True)
    visible = models.BooleanField(default=True)
    order = models.AutoField(primary_key=True)
    
class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    visible = models.BooleanField(default=True)
    years = models.IntegerField(default=1) 
    order = models.AutoField(primary_key=True)

class Resume(models.Model):
    file = models.FileField(upload_to='portfolio/files/')
    date = models.DateField(auto_now_add=True)
    selected = models.BooleanField(default=False)

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if self.selected:
            Resume.objects.filter(selected=True).update(selected=False)
        super().save(force_insert, force_update, using, update_fields)

    def delete(self, using: Any = ..., keep_parents: bool = ...) -> tuple[int, dict[str, int]]:
        if self.selected:
            new_selected_resume = Resume.objects.first()
            if new_selected_resume:
                new_selected_resume.selected = True
                new_selected_resume.save()
        super().delete(using, keep_parents)