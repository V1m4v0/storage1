from django.shortcuts import render

def func_template(request):
    return render(request, template_name='func_template')

