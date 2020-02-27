# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # Create your models here.
# STATUS = (
#     (0, "blocked"),
#     (1, "Active")
# )
# class Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     status = models.IntegerField(choices=STATUS, default=1)
#     def __str__(self):
#         return '{} status to {}'.format(self.user, self.status)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
