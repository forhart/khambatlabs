from django.db import models

# Create your models here.

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class Patient(models.Model):
    first_name  = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=200)
    gender      = models.CharField(max_length=1,choices=GENDER_CHOICES)
    age         = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.first_name+" "+self.last_name

    class Meta:
        ordering = ['first_name']


class Doctor(models.Model):
    first_name  = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=200)
    gender      = models.CharField(max_length=1,choices=GENDER_CHOICES)
    age         = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return ("Dr. %s %s") % (self.first_name,self.last_name)
    
class Hospital(models.Model):
    name        = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return "%s Hospital " % (self.name)

class Test(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField();

    def __unicode__(self):
        return "%s / %s " % (self.name,self.price)
 

class Sample(models.Model):
    Taken    =   models.DateTimeField()
    patient  =   models.ForeignKey('Patient')
    doctor   =   models.ForeignKey('Doctor')
    hospital = models.ForeignKey('Hospital')
    test     = models.ManyToManyField(Test)
    def __unicode__(self):
        return "Sample"

    def list_tests(self):
       all_tests =  self.test.get_query_set()
       test_list = []
       for each_test in all_tests:
           test_list.append(each_test.name)
       return ",".join(test_list)

    def count_tests(self):
        return len(self.test.get_query_set()) 
        count_tests.short_description = "Count"
        
