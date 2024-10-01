from django.shortcuts import redirect, render
from .models import Ikasle
from .forms import IkasleForm

# Create your views here.
def ikasle_list(request):
    ikasleZerrenda=Ikasle.objects.all()
    return render(request, 'FirstApp/ikasle_list.html',{'ikasleak':ikasleZerrenda})

def ikasle_new(request):
    if request.method == 'POST':
        form=IkasleForm(request.POST)
        if form.is_valid:
            ikasle = form.save()
            ikasle.save()
        return redirect('zerrenda-default')
    else:
        form=IkasleForm()
        return render(request, 'FirstApp/ikasle_new.html', {'form':form})