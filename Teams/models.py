from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=225,blank=False,null=False,unique=True)
    wins  = models.IntegerField(blank=True,null=True,default=0)
    losses =  models.IntegerField(blank=True,null=True,default=0)
    tie = models.IntegerField(blank=True,null=True,default=0)
    score = models.IntegerField(blank=True,null=True,default=0)
    played_Count = models.IntegerField(blank=True,null=True,default=0)

    def save(self, *args, **kwargs): 
        self.score = 3*self.wins + 1*self.tie
        super(Teams, self).save(*args, **kwargs) 


class TeamScoring(models.Model):
    option = (
        ('wins','wins'),
        ('loss','loss'),
        ('ties','ties'),
    )
    options = models.CharField(max_length=30,blank=False,null=False,choices=option)
    Teams = models.ForeignKey(Teams,on_delete=models.CASCADE)