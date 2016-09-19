from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(model.Model):
	create = models.DateTimeField(auto_now_add=True)
	title = models.Charfield(max_length=100, blank=True, default='')
	code = models.TextField()
	lineos = models.BooleanField(default=False)
	language = models.Charfield(choides=LANGUAGE_CHOICES, default='python', max_length=100)
	styles = models.Charfield(choides=LANGUAGE_STYLES, default='styles', max_length=100)



# Create your models here.
