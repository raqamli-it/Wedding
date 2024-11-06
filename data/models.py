from django.db import models


class BackgroundImage(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='story/')
    create_time = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqti avtomatik ravishda saqlanadi

    def __str__(self):
        return self.title


class Story(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='story/')
    create_time = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqti avtomatik ravishda saqlanadi

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='story/')
    create_time = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqti avtomatik ravishda saqlanadi

    def __str__(self):
        return self.title


class Attending(models.Model):
    name = models.CharField(max_length=500)
    gmail = models.EmailField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqti avtomatik ravishda saqlanadi

    def __str__(self):
        return self.name


class Message(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.EmailField(max_length=500)
    message = models.TextField(1500)
    create_time = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqti avtomatik ravishda saqlanadi

    def __str__(self):
        return self.first_name

class MyFotos(models.Model):
    man_image = models.ImageField(upload_to='man_image/')
    woman_image = models.ImageField(upload_to='woman_image/')
