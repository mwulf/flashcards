from django.db import models

# for first iteration:
# card has entry and definition
# so as to keep it very simple

# for next iteration, modify so that one card can contain many definitions

class Card(models.Model):
    entry = models.CharField(max_length=200)
    definition = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.entry
