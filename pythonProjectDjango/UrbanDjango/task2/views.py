from django.shortcuts import render

def func_template(request):
    return render(request, 'func_template.html')
