from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ungettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    '''
    already exist:
    {
        username
        password
        first name
        last name
        email
    }
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #! show phone
    phone_number = models.CharField(max_length=10, blank=True, null=True) #! change to False
    #! region
    #! city
    #! type
    #! major
    #! rank
    #! show desire
    #! desire
    #! text field for Notes
    
    

    def __str__(self):
        return str(self.user)

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )