from django.db import models





class ColourModel(models.Model):

    colour=models.CharField(max_length=254)

    def __str__(self):
        return f"{self.colour}"


class WineModel(models.Model):
    """ model for wines"""
    name = models.CharField(max_length=254)
    strain = models.CharField(max_length=254)
    colour = models.ForeignKey(ColourModel, on_delete=models.CASCADE)
    image = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.name}"



