from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import BackgroundImage, Story, Gallery, Attending, Message, MyFotos


def index(request):
    bek_image = BackgroundImage.objects.filter(id=1).first()
    recent_stories = Story.objects.all().order_by('-create_time')[:4]
    my_fotos = MyFotos.objects.filter(id=1).first()
    context = {
        'bek_image': bek_image,
        'recent_stories': recent_stories,
        'my_fotos': my_fotos
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')

        if name and gmail:
            Attending.objects.create(name=name, gmail=gmail)
            return HttpResponseRedirect(request.path)  # Foydalanuvchini o'z sahifasiga qaytarish
        else:
            return render(request, 'index.html', {'error': "Iltimos, hamma maydonlarni to'ldiring."})

    return render(request, 'index.html', context)


def gallery(request):
    galleries = Gallery.objects.all()
    my_fotos = MyFotos.objects.filter(id=1).first()

    context = {
        'galleries': galleries,
        'my_fotos': my_fotos
    }
    return render(request, 'gallery.html', context)


def about(request):
    recent_stories = Story.objects.all().order_by('-create_time')
    my_fotos = MyFotos.objects.filter(id=1).first()

    context = {

        'recent_stories': recent_stories,
        'my_fotos': my_fotos
    }
    return render(request, 'about.html', context)


def contact(request):
    my_fotos = MyFotos.objects.filter(id=1).first()

    context = {
        'my_fotos': my_fotos
    }
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        message = request.POST.get('message')

        if first_name and last_name and message:
            Message.objects.create(first_name=first_name, last_name=last_name, message=message)
            return HttpResponseRedirect(request.path)
        else:
            return render(request, 'contact.html', {'error': "Iltimos, hamma maydonlarni to'ldiring."})

    return render(request, 'contact.html', context)





