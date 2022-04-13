from django.contrib.auth import views as auth_views, get_user_model, login

from django.contrib.auth import forms as auth_forms
from django.views import generic as views

from petstagram.accounts.forms import CreateProfileForm
from petstagram.main.models import Pet, PetPhoto

UserModel = get_user_model

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.models import Profile
from petstagram.common.view_mixins import RedirectToDashboard


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')

    # регистриране и логване след това
    def form_valid(self, form):
        result = super().form_valid(form)
        # user = self.object
        # request = self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    form_class = auth_forms.AuthenticationForm
    template_name = 'accounts/login_page.html'
    next_page = reverse_lazy('dashboard')


class EditProfileView(views.UpdateView):
    pass


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'







class ProfileView(views.DetailView):
    model = Profile
    template_name = 'main/../../templates/accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # self object is a Profile
        pets = Pet.objects.filter(user_id=self.object.user_id)
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_pet_photos_count = len(pet_photos)

        context.update({
            'pets': pets,
            'total_likes_count': total_likes_count,
            'total_pet_photos_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
        })

        return context




class CreateProfileView(views.CreateView):
    pass


class DeleteProfileView(views.DeleteView):
    pass
