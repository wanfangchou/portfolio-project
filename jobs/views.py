from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    # grab objects from database, and return the dictionary
    return render(request, 'jobs/home.html', {'jobs':jobs})
