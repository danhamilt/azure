from django.db import models

# Create your models here.
class ChatSituation(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    def __str__(self):
        return self.text

# sits = ["I was at a restaurant and my ex texted me", "I felt like my boss doesn't notice me", "my friend always cancels my plans"]