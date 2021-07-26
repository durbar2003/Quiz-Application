from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    def __str__(self):
        return f'{self.name} ({self.address})'

class Answer(models.Model):
    answer=models.TextField()

    def __str__(self):
        return self.answer    

class Participant(models.Model):
    name=models.TextField()
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Quiz(models.Model):
    question=models.TextField()
    ans=models.TextField(null=True)

    def __str__(self):
        return self.question

class Meetup(models.Model):
    title=models.CharField(max_length=200)
    organizer_email=models.EmailField()
    date_n_time=models.DateTimeField()
    slug=models.SlugField(unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    quiz=models.ManyToManyField(Quiz)
    user_response=models.TextField()
    participants=models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self):
        return f'{self.title}-{self.slug}'