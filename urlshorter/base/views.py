from django.shortcuts import render, redirect
from .models import Urls
import shortuuid
from django.http import HttpResponse

# Create your views here.
def home(request):
    newUrl = Urls.objects.all()
    if request.method == 'POST':
        newUrl = Urls.objects.create(
            id = shortuuid.ShortUUID().random(length=7),
            long_url = request.POST.get('long_url'),
        )
        newUrl.save()
        return redirect(newUrl.long_url)
    
    context = {'long_url': newUrl,"currectUrl":request}
    return render(request,'home.html',context)

def redirect_to_url(request,pk):
    url_object  = Urls.objects.get(id=pk)
    url_object.no_clicks = url_object.no_clicks + 1
    url_object.save()
    
    return redirect(url_object.long_url)