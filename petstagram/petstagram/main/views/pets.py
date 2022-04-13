from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

# Create your views here.
from petstagram.main.forms.pet_forms import CreatePetForm, EditPetForm, DeletePetForm


# def pet_action(request, class_form, success_url, instance, template_name):
#     if request.method == 'POST':
#         form = class_form(request.POST, instance=instance)
#         if form.is_valid:
#             form.save()
#             return redirect(success_url)
#     else:
#         form = class_form(instance=instance)
#     context = {
#         'form': form,
#         'pet': instance,
#     }
#     return render(request, template_name, context)
from petstagram.main.models import Pet, PetPhoto


class CreatePetView(views.CreateView):
    form_class = CreatePetForm
    template_name = 'main/pet_create.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    model = Pet
    form_class = EditPetForm
    template_name = 'main/pet_edit.html'
    success_url = reverse_lazy('dashboard')


class DeletePetView(views.DeleteView):
    form_class = DeletePetForm
    template_name = 'main/pet_delete.html'

# def create_pet_page(request):
#     return pet_action(request, CreatePetForm, 'profile', Pet(user_profile=get_profiles()), 'pet_create.html')
#
#
# def edit_pet_page(request, pk):
#     return pet_action(request, EditPetForm, 'profile', Pet.objects.get(pk=pk), 'pet_edit.html')
#
#
# def delete_pet_page(request, pk):
#     return pet_action(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'pet_delete.html')
