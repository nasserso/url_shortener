from django.db import models

import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class Shortener(models.Model):
    slang = models.SlugField(max_length=50, default=randomword(10))
    original_link = models.URLField(max_length=200)
    access_counter = models.IntegerField(default=0)
