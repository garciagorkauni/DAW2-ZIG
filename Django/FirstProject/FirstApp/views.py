from django.shortcuts import redirect, render
from .models import Ikasle, Nota, Ikasgaia
from .forms import IkasleForm, NotaForm, IkasgaiForm

# Create your views here.
def ikasle_list(request):
    ikasleZerrenda=Ikasle.objects.all()
    return render(request, 'FirstApp/kudeaketa/ikasle/ikasle_list.html',{'ikasleak':ikasleZerrenda})

def ikasle_new(request):
    if request.method == 'POST':
        form=IkasleForm(request.POST)
        if form.is_valid:
            ikasle = form.save()
            ikasle.save()
        return redirect('zerrenda-default')
    else:
        form=IkasleForm()
        return render(request, 'FirstApp/kudeaketa/ikasle/ikasle_new.html', {'form':form})
    
def nota_list(request):
    notaZerrenda=Nota.objects.all()
    return render(request, 'FirstApp/kudeaketa/nota/nota_list.html',{'notak':notaZerrenda})

def nota_new(request):
    if request.method == 'POST':
        form=NotaForm(request.POST)
        if form.is_valid:
            nota = form.save()
            nota.save()
        return redirect('nota-list')
    else:
        form=NotaForm()
        return render(request, 'FirstApp/kudeaketa/nota/nota_new.html', {'form':form})
    
def ikasgai_list(request):
    ikasgaiZerrenda=Ikasgaia.objects.all()
    return render(request, 'FirstApp/kudeaketa/ikasgai/ikasgai_list.html',{'ikasgaiak':ikasgaiZerrenda})

def ikasgai_new(request):
    if request.method == 'POST':
        form=IkasgaiForm(request.POST)
        if form.is_valid:
            ikasgaia = form.save()
            ikasgaia.save()
        return redirect('ikasgai-list')
    else:
        form=IkasgaiForm()
        return render(request, 'FirstApp/kudeaketa/ikasgai/ikasgai_new.html', {'form':form})