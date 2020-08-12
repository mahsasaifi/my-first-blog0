#from  oder import Anweisungen um Sachen aus anderen Dateien mitzunuten
from django.conf import settings
from django.db import models
from django.utils import timezone

# definiert unser Model -> Objektvorlage; class = Klasse; Post = Name des Modells kann beliebig sein; models.Models = gibt an das Post-Model ein Django-Modell ist, so weiß Django das es in Datenbank gespeichert werden soll
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#veröffentlichung 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
