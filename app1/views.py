from django.shortcuts import render

# Create your views here.
def nvn(request):
    d={'username':'nvn'}
    return render(request,'Login form.html',context=d)
