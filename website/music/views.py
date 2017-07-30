from .models import Album,Song
from django.shortcuts import render,get_list_or_404

def index(request):
    
    all_album = Album.objects.all()
    #dictonary
    context={
        'all_album':all_album
    }
    return render(request,'music/index.html',{'all_album':all_album})

def details(request,album_id):
    #album=Album.objects.get(pk=album_id) without this one 
    #getting error for 404 in shortcut
    album=get_list_or_404(Album,pk=album_id)
    
    return render(request,'music/details.html',{'album':album})

def favorite(request,album_id):
   
    album=get_list_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/details.html',{'album':album,'error_message':error_message})
    else:
        selected_song.is_favorite=True
        selected_song.save()
    
        return render(request, 'music/details.html', {'album': album})