from django.shortcuts import render

# Create your views here.
def index(request):
    # hello
    return render(request, 'index.html')