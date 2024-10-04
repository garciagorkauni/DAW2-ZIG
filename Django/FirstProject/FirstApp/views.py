from django.shortcuts import get_object_or_404, redirect, render
from .models import Ikasle, Nota, Ikasgaia
from .forms import IkasleForm, NotaForm, IkasgaiForm, EditNotaForm

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

def delete_ikasle(request):
    if request.method == 'POST':
        uid = request.POST.get("uid", "")
        Ikasle.objects.filter(id=uid).delete()
        return redirect('zerrenda-default')
    
    else:
        ikasleZerrenda=Ikasle.objects.all()
        return render(request, 'FirstApp/kudeaketa/ikasle/delete_ikasle.html',{'ikasleak':ikasleZerrenda})

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
    
def edit_nota(request):
    if request.method == 'POST':
        nid = request.POST.get("nid", "")
        nota = request.POST.get("nota", "")
        oharra = request.POST.get("oharra", "")
        nota = Nota.objects.get(id=nid)
        nota.nota = nota
        nota.oharra = oharra
        nota.save()

        return redirect('nota-list')
    
    else:
        notaZerrenda=Nota.objects.all()
        return render(request, 'FirstApp/kudeaketa/nota/edit_nota.html',{'notak':notaZerrenda})

def edit_nota_form(request, ikasle_id, ikasgai_id):
    ikasle = get_object_or_404(Ikasle, id=ikasle_id)
    ikasgaia = get_object_or_404(Ikasgaia, id=ikasgai_id)
    nota = get_object_or_404(Nota, ikasle=ikasle, ikasgaia=ikasgaia)

    if request.method == 'POST':
        form = EditNotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('nota-list')
    else:
        form = EditNotaForm(instance=nota)

    return render(request, 'FirstApp/kudeaketa/nota/nota_new.html', {'form': form})


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