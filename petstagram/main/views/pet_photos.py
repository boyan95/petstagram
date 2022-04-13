from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from petstagram.main.models import PetPhoto, Pet

from django.views import generic as views


# def show_pet_photo(request, pk):
#     pet_photo = PetPhoto.objects.get(pk=pk)
#
#     context = {
#         'pet_photo': pet_photo,
#     }
#     return render(request, 'main/photo_details.html', context)


class PetPhotoDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('tagged_pets')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


def likes_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    if pet_photo.likes == 0:
        pet_photo.likes += 1
        pet_photo.save()
    return redirect('pet photo details', pk)


class CreatePetPhotoView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = PetPhoto
    template_name = 'main/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(views.UpdateView):
    model = PetPhoto
    template_name = 'main/photo_edit.html'
    fields = ('description',)

    def get_success_url(self):
        return reverse_lazy('pet photo details', kwargs={'pk': self.object.id})

    # def create_photo_page(request):
    #     return render(request, 'main/photo_create.html')
    #
    #
    # def edit_photo_page(request):
    #     return render(request, 'main/photo_edit.html')
