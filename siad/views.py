from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from siad.models import Aspirante
import csv

# Create your views here.
def index(request):
	return render(request, 'siad/index.html', {})

def atributos_meta(request): 
	valor = request.META.items() 
	valor.sort() 
	html = [] 
	for k, v in valor: 
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v)) 
	return HttpResponse('<table>%s</table>' % '\n'.join(html)) 

def formulario_buscar(request):
	return render(request, 'siad/formulario_buscar.html')

def buscar(request): 
	error = False 
	if 'q' in request.GET: 
		q = request.GET['q'] 
		if not q: 
			error = True 
		else: 
			libros = Aspirante.objects.filter(nombre__icontains=q) 
			return render(request, 'siad/resultados.html', {'aspirantes': libros, 'query': q}) 
 
	return render(request, 'siad/formulario_buscar.html', {'error': error}) 


def contactos(request): 
    if request.method == 'POST': 
        form = FormularioContactos(request.POST) 
        if form.is_valid(): 
            cd = form.cleaned_data 
            send_mail( 
                cd['asunto'], 
                cd['mensaje'], 
                cd.get('email', 'noreply@example.com'), 
                    ['siteowner@example.com'], 
             ) 
            return HttpResponseRedirect('/contactos/gracias/') 
    else: 
        form = FormularioContactos() 
    return render(request, 'formmulario_contactos.html', {'form': form})

def control_escolar(request):
    return render(request,'siad/control_escolar.html')

def contabilidad(request):
    return render(request,'siad/contabilidad.html')

def promotoria(request):
	lista_prospectos_total = Aspirante.objects.order_by("id")
	lista_prospectos = Aspirante.objects.order_by("id")[0:10]
	i=10
	grupo = round(len(lista_prospectos_total) // i)
	resto= round(len(lista_prospectos_total) % i)
	paginas = grupo+resto
	j=1
	inicio=0
	fin=1
	if j < paginas:
		j=j+1
		inicio=fin-1
		fin=inicio+i
		lista_prospect_p1 = Aspirante.objects.order_by("id").filter(id__range=(inicio, fin))
		pass
	elif resto < i:
		inicio=fin-1
		fin=inicio+i
		lista_prospect_p1 = Aspirante.objects.order_by("id").filter(id__range=(inicio, resto))
		pass
	return render_to_response('siad/formulario_buscar.html', {'lista_prospect_p1':lista_prospect_p1,'lista_prospectos_total':lista_prospectos_total,'lista_prospectos':lista_prospectos, 'paginas':paginas, 'i':i})