from django.shortcuts import get_object_or_404, redirect, render
from .models import Pazientea, Medikua, Zita
from .forms import PazienteaForm, MedikuaForm, ZitaForm

# Default view
def base(request):
    return render(request, 'osakidetza/base.html')

# CRUD for Pazientea
def new_pazientea(request):
    if request.method == 'POST':
        form=PazienteaForm(request.POST)
        if form.is_valid:
            pazientea = form.save()
            pazientea.save()
        return redirect('base')
    else:
        form=PazienteaForm()
        return render(request, 'osakidetza/pazientea/pazientea_new.html', {'form':form})

def delete_pazientea(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        Pazientea.objects.filter(id=id).delete()
        return redirect('base')
    
    else:
        pazienteZerrenda=Pazientea.objects.all()
        return render(request, 'osakidetza/pazientea/pazientea_delete.html',{'pazienteak':pazienteZerrenda})

def edit_pazientea(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        pazientea = Pazientea.objects.get(id=id)
        pazientea.izena = request.POST.get("izena", pazientea.izena)
        pazientea.abizena = request.POST.get("abizena", pazientea.abizena)
        pazientea.telefonoa = request.POST.get("telefonoa", pazientea.telefonoa)
        pazientea.save()

        return redirect('base')
    
    else:
        pazienteZerrenda=Pazientea.objects.all()
        return render(request, 'osakidetza/pazientea/pazientea_edit.html',{'pazienteak':pazienteZerrenda})

def edit_pazientea_form(request, pazientea_id):
    pazientea = get_object_or_404(Pazientea, id=pazientea_id)

    if request.method == 'POST':
        form = PazienteaForm(request.POST, instance=pazientea)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = PazienteaForm(instance=pazientea)

    return render(request, 'osakidetza/pazientea/pazientea_new.html', {'form': form})

# CRUD for Medikua
def new_medikua(request):
    if request.method == 'POST':
        form=MedikuaForm(request.POST)
        if form.is_valid:
            medikua = form.save()
            medikua.save()
        return redirect('base')
    else:
        form=MedikuaForm()
        return render(request, 'osakidetza/medikua/medikua_new.html', {'form':form})

def delete_medikua(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        Medikua.objects.filter(id=id).delete()
        return redirect('base')
    
    else:
        medikuZerrenda=Medikua.objects.all()
        return render(request, 'osakidetza/medikua/medikua_delete.html',{'medikuak':medikuZerrenda})

def edit_medikua(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        medikua = Medikua.objects.get(id=id)
        medikua.izena = request.POST.get("izena", medikua.izena)
        medikua.abizena = request.POST.get("abizena", medikua.abizena)
        medikua.telefonoa = request.POST.get("telefonoa", medikua.telefonoa)
        medikua.save()

        return redirect('base')
    
    else:
        medikuZerrenda=Medikua.objects.all()
        return render(request, 'osakidetza/medikua/medikua_edit.html',{'medikuak':medikuZerrenda})
    
def edit_medikua_form(request, medikua_id):
    medikua = get_object_or_404(Medikua, id=medikua_id)

    if request.method == 'POST':
        form = MedikuaForm(request.POST, instance=medikua)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = MedikuaForm(instance=medikua)

    return render(request, 'osakidetza/medikua/medikua_new.html', {'form': form})

# CRUD for Zita
def new_zita(request):
    if request.method == 'POST':
        form=ZitaForm(request.POST)
        if form.is_valid:
            zita = form.save()
            zita.save()
        return redirect('base')
    else:
        form=ZitaForm()
        return render(request, 'osakidetza/zita/zita_new.html', {'form':form})