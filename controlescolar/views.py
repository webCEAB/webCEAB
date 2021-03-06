from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .models import Estudiante
from .forms import NuevoAlumno,NuevoAlumno2

def consulta_adeudos(request,min = None):
	queryset = Estudiante.objects.filter(adeudo__gte = min)
	context = {
		"object_list": queryset, 
	}
	print queryset
	return render(request, "controlescolar/busqueda.html", context)

def control_escolares(request):
	lista_alumnos_total = Estudiante.objects.order_by("id")
	return render_to_response('controlescolar/formulario_buscar_alumno.html', {'lista_alumnos_total':lista_alumnos_total})


def formulario_buscar_alumno(request):
	return render(request, 'controlescolar/formulario_buscar_alumno.html')

def buscar_alumnos(request): 
	error = False 
	if 's' in request.GET: 
		s = request.GET['s'] 
		if not s: 
			error = True 
		else: 
			alumnos = Estudiante.objects.filter(id__icontains=s) 
			return render(request, 'controlescolar/resultados_alumno.html', {'alumnos': alumnos, 'query': s}) 
 
	return render(request, 'controlescolar/formulario_buscar_alumno.html', {'error': error}) 

def nuevo_alumno(request):
	if request.method == 'POST':
		form = NuevoAlumno2(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('control_escolares')
	else:
		form = NuevoAlumno2()
	return render(request, 'controlescolar/nuevo_alumno.html', {'form': form})

def edit_estudiante(request, id_estudiante):
	estudiante=Estudiante.objects.get(id=id_estudiante)
	if request.method == 'GET':
		form = NuevoAlumno(instance=estudiante)
	else:
		form = NuevoAlumno(request.POST, instance=estudiante)
		if form.is_valid():
			form.save()
		return redirect('control_escolares')
	return render(request, 'controlescolar/control_escolar.html', {'form': form})