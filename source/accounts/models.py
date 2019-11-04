
from django.db import models
from django.contrib.auth.models import User

# DEFAULT_AVATAR = "/uploads/user_pics/default_avatar.jpg"


class Profile(models.Model):

    DEFAULT_AVATAR = "/uploads/user_pics/default_avatar.jpg"

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, verbose_name="Пользователь")
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name="Аватар")
    about = models.TextField(max_length=3000, null=True, blank=True, verbose_name="О себе")
    github = models.URLField(null=True, blank=True, verbose_name="Профиль Github")

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

