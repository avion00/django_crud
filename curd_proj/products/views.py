from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect after form submission
            return redirect('home')  # Redirect to the same view (home)
    else:
        form = ImageForm()
    
    img = Image.objects.all()
    return render(request, 'index.html', {'img': img, 'form': form})
