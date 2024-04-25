from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def employer(request):
    return render(request, "employer.html")

def vacantions(request):
    return render(request, "vacantions.html")
