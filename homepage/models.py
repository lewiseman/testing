from django.db import models


class MainTag(models.Model):
    main_tag = models.CharField(max_length=50)

    def __str__(self):
        return self.main_tag



class SubTag(models.Model):
    sub_tag = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_tag



class Hadithi(models.Model):
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='stories', null=True, default=1)
    title = models.CharField(max_length=500, null=True)
    date = models.DateTimeField()
    story = models.TextField()
    category = models.ManyToManyField(MainTag)
    tag = models.ManyToManyField(SubTag)
    viewers = models.IntegerField(null=True, default=0)
    positive_clicks = models.IntegerField(null=True, default=0)
    negative_clicks = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hadithi"
        verbose_name_plural = "Stories"


class DemoStories(models.Model):
    title = models.TextField()
    author = models.TextField()
    rated = models.TextField()
    posted = models.TextField()
    tags = models.TextField()
    story = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Demo"
        verbose_name_plural = "DemoStories"