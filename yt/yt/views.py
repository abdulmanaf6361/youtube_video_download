from pytube import YouTube

from django.shortcuts import render
from django.http import HttpResponse


def homePage(request):
    return render(request, 'index.html')

def views(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        # Perform the logic to produce the new URL  
        yt = YouTube(url)
        streams = yt.streams.all()
        stream = streams[2]
        link = stream.url
        
        
        # jn
        new_url = link
        return render(request, 'index.html', {'new_url': new_url})
    else:
        return render(request, 'index.html')

