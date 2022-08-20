from django.db import models
from PIL import Image

# Create your models here.



class Agent(models.Model):
    agent_first_name = models.CharField(max_length=255, blank=False)
    agent_last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    address = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=255, blank=False)
    MALE = "M"
    FEMALE = "F"
    sex_choices = [(MALE, 'male'), (FEMALE, 'female')]
    sex = models.CharField(max_length=2, choices=sex_choices, default=MALE)
    image = models.ImageField(default='default.png', upload_to='agent_pics')

    def __str__(self):
        return (f'{self.agent_first_name} {self.agent_last_name}')



class Cards(models.Model):
    card_title = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    realtor = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.png', upload_to='cards_pics')

    def __str__(self):
        return self.card_title

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 and img.width > 300:
            img_output = (300,300)
            img.resize(300,300)
            img.save(self.image.path)
