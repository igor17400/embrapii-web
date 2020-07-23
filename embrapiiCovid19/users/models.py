from django.db import models
from django.urls import reverse


class TestType(models.Model):
    #RT-PCR, Sorologia, Teste Rápido - Antígenos, Teste Rápido - Anticorpos
    name = models.CharField(max_length=50, default='RT-PCR')

    def __str__(self):
        return self.name
        

    

class User(models.Model):
    name = models.CharField(max_length=200)
    born_date = models.DateField()
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])

    