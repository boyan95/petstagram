import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from petstagram.accounts.models import PetstagramUser
from petstagram.common.validators import validate_file_max_size_in_mb

UserModel = get_user_model()





'''
•	The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
•	The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
•	Profile picture - the user can link their picture using a URL.
The user may provide the following information in their profile:
•	Date of birth: day, month, and year of birth.
•	Description - a user can write any description about themselves, no limit of words/chars.
•	Email - a user can only write a valid email address.
•	Gender - the user can choose one of the following: "Male", "Female", and "Do not show".
'''


class Pet(models.Model):
    # constants
    NAME_MAX_LENGTH = 30
    MIN_DATE_OF_BIRTH = datetime.date(1920, 1, 1)

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    # fields(columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,

    )
    # one-to-one

    # one-to-many
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'

    # many-to-many
    # properties
    def age(self):
        if self.date_of_birth:
            return datetime.datetime.now().year - self.date_of_birth.year
        return None

        # methods

    # dunder methods
    # Meta
    class Meta:
        unique_together = ('user', 'name')


'''
The user must provide the following information when adding a pet in their profile:
•	Name - it should consist of maximum 30 characters. All pets' names should be unique for that user.
•	Type - the user can choose one of the following: "Cat", "Dog", "Bunny", "Parrot", "Fish", or "Other".
The user may provide the following information when adding a pet to their profile:
•	Date of birth - pet's day, month, and year of birth.
'''


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            validate_file_max_size_in_mb,
        )
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least 1 pet
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    date_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )

    # likes = models.ForeignKey(
    # Like
    # )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.photo}'







