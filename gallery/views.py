from django.shortcuts import render,redirect
from .models import Images
from .forms import Uploadform

# Create your views here.
def gallery(request):
    if request.method == 'POST':
        form = Uploadform(request.POST,request.FILES)
        if form.is_valid():
            animal = form.cleaned_data.get('animal')
            img = form.cleaned_data.get('img_file')
            img_obj = Images.objects.create(img = img, animal = animal)
            img_obj.save()
    
        return redirect('gallery')
    else:
        form = Uploadform()
        obj_lists = Images.objects.order_by('-date')
        context = {
            'Images':obj_lists,
            'form': form
        }
        return render(request,'gallery/gallery.html',context)