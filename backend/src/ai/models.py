from django.db import models

class Range(models.Model):
    
    feature_name1 = models.CharField(max_length=25)
    feature_name2 = models.CharField(max_length=25)

    sub_value1 = models.FloatField()
    sub_value2 = models.FloatField()

    # left boder of R
    l_R = models.FloatField(default=0)
    # right border og R
    r_R = models.FloatField(default=0)

    # For taking the last updates from db
    udapte_number = models.IntegerField(default=1)

    def __str__(self):
        return self.feature_name1 + "; " + self.feature_name2