from django.urls import path


from petstagram.main.views.generic import *
from petstagram.main.views.pets import *
from petstagram.main.views.profiles import *
from petstagram.main.views.pet_photos import *

urlpatterns = (
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # profile

    # pet
    path('pet/add/', CreatePetView.as_view(), name='create pet page'),
    path('pet/edit/<int:pk>', EditPetView.as_view(), name='edit pet page'),
    path('pet/delete/<int:pk>', DeletePetView.as_view(), name='delete pet page'),
    # pet_photo
    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/liked/<int:pk>/', likes_pet_photo, name='likes pet photo'),
    path('photo/add/', CreatePetPhotoView.as_view(), name='create photo page'),
    path('photo/edit/<int:pk>', EditPetPhotoView.as_view(), name='edit photo page'),

)
