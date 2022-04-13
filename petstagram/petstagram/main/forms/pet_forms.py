from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.main.models import Pet
from petstagram.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_control()

    def save(self, commit=True):
        # получаваме пет инстацията, не отива към базата
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth < self.MIN_DATE_OF_BIRTH or self.MAX_DATE_OF_BIRTH < date_of_birth:
            raise ValidationError(
                f'Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}!')
        return date_of_birth

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            )
            # ),
            # 'type': forms.ChoiceField(
            #     choices=Pet.TYPES
            # ),
            # 'date_of_birth': forms.DateInput(
            #     attrs={
            #         'min': '1920-01-01',
            #     }
            # )
        }


class EditPetForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth < self.MIN_DATE_OF_BIRTH or self.MAX_DATE_OF_BIRTH < date_of_birth:
            raise ValidationError(
                f'Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}!')
        return date_of_birth

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')


class DeletePetForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    # као искам само name да е disabled казвам
    # disabled_fields = ('name',)
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        exclude = ('user_profile',)
