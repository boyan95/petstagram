from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram.accounts.managers import PetstagramUserManager
from petstagram.common.validators import only_letters_validator

'''
custom user

1. Create model extending...
2. Config this model in settings.py
3. Create user manager

'''


# UserModel = get_user_model()
# user = UserModel


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25
    # AbstractBaseUser - contains password, last_login, save() which turn the password in the right way and MORE
    # PermissionsMixin - is_superuser, groups, user_permissions
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 25
    PASSWORD_MAX_LENGTH = 25
    CONFIRM_PASSWORD_MAX_LENGTH = 25

    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    '''
    GENDERS = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Do not show', 'Do not show'),
    ]
    '''

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    picture = models.URLField()
    birth_day = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,

    )
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=max(len(x) for (x, _) in GENDERS),
        choices=GENDERS,

        # if value == 'Male' => bad
        # if value == Profile.MALE => good
    )
    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,

    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
