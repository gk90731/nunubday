from django.shortcuts import render

# Create your views here.
def index(request):
    index = {'index_page':'INDEX PAGE'}
    return render(request,'index.html',context = index)
