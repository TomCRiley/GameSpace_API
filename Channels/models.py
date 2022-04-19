from django.db import models

# Create your models here.


class Developer(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Platform(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):

    title = models.CharField(max_length=60)
    developer = models.ForeignKey(
        Developer, related_name='developer', on_delete=models.CASCADE)
    platform = models.ManyToManyField(
        Platform, related_name='platform')  # add on_delete CASCADE to the through model
    image = models.CharField(max_length=200)
    release_date = models.DateField(null=True)

    def __str__(self):
        return self.title


# e.g. gamr.io/superMario64 - associated Game, Dev and Platform.
class Channel(models.Model):

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    createdDate = models.DateField(null=True)
    image = models.CharField(max_length=200)

    # models.PROTECT = avoid deleting the gameChannel if the game/platform/dev is deleted in the game/platform/dev model
    game = models.ForeignKey(Game, related_name='games',
                             on_delete=models.PROTECT)
    platform = models.ForeignKey(
        Platform, related_name="platforms", on_delete=models.PROTECT)
    developer = models.ForeignKey(
        Developer, related_name='developers', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.createdDate}'