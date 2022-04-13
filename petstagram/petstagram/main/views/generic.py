from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import PetPhoto, Pet

from django.views import generic as views

UserModel = get_user_model()
user = UserModel


# def show_home_page(request):
#     context = {
#         'hide_additional_nav_bar': True,
#     }
#     return render(request, 'main/home_page.html', context)

class HomePageView(RedirectToDashboard,views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_bar'] = True
        return context



class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'


# def show_dashboard(request):
#     gotten_profile = get_profiles()
#     # if not gotten_profile:
#     #     return redirect('401')
#     # pet_set идва от models.py class Pet, защото в user_profile сме задали foreign_key с Profile и то автоматично генерира pet_set
#     pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(
#         tagged_pets__user_profile=gotten_profile).distinct()
#     context = {
#         'pet_photos': pet_photos,
#     }
#     return render(request, 'main/dashboard.html', context)
