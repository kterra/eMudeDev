from django.shortcuts import render


# Views for the eMude Core app.
def index(request):
    context_dict = {}
    return render(request, "core/index.html", context_dict)

def login(request):
    context_dict = {}
    return render(request, "core/login.html", context_dict)
