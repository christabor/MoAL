from django.db import models


class JobCategory(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        fields = ['name']
        return unicode('<{}>'.format(*fields))


class Job(models.Model):
    name = models.CharField(max_length=50)
    avg_salary = models.IntegerField()
    category = models.ForeignKey(JobCategory)

    def __unicode__(self):
        fields = ['category', 'avg_salary', 'name', ]
        return unicode('<{}.{}.{}.>'.format(*fields))
