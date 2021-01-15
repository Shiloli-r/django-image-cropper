from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm


# Create your views here.
def home(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PhotoForm()
    context = {
        'form': form,
        'photo': photos
    }
    return render(request, 'index.html', context)
