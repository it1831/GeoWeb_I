from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.html import format_html

# Create your models here.

def picture_path(instance, filename):
    return "Cyklo/" + str(instance.id) + "/picture/" + filename

class Type(models.Model):
    bike_type = models.CharField(max_length=50, unique=True, verbose_name="Bike type", help_text='Enter a bike type (mtb, road, gravel etc)')

    class Meta:
        ordering = ["bike_type"]

    def __str__(self):
        return self.bike_type

    def cyklo_counting(self, obj):
        return obj.cyklo_set.count()


class Cyklo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    type = models.ManyToManyField(Type, help_text='Select a type for this bike')
    picture = models.ImageField(upload_to=picture_path, blank=True, null=True, verbose_name="Picture")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    release_date = models.DateField(blank=True, null=True ,help_text="Please use the following format: <em>YYYY-MM-DD</em>.", verbose_name="Release date")
    rate = models.FloatField(null=True, default=5.0, validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], help_text="Please enter an float value (range 1.0 -10.0)", verbose_name="Rate")

    class Meta:

        ordering = ["-release_date", "name"]

    def __str__(self):
        return f"{self.name}, year: {str(self.release_date.year)}, rate: {str(self.rate)}"

    def get_absolute_url(self):
        return reverse('cyklo-detail', args=[str(self.id)])

    def release_year(self):
        return self.release_date.year

    def rate_percent(self):
        return format_html("{} %", int(self.rate * 10))
