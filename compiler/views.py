from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import CompilerUtils
from .CompilerUtils import Compiler


# Create your views here.
executor = Compiler()

def testpage(request):
    template_data = {}
    if request.method == 'POST':
        if 'submit_code' in request.POST:
            form = forms.CodeExecutorForm(request.POST)
            if form.is_valid():
                code = form.cleaned_data['code']

                executor.set_code(code)
                
                execution_result = executor.execute()

                executor.delete_code_file()

                return HttpResponse("Worked!")
                
            else:
                return HttpResponse("Cannot sanitize form data")

        elif 'terminate_code' in request.POST:
            executor.terminate()
            return HttpResponse("Terminated!")
        form = forms.CodeExecutorForm(request.POST)
        if form.is_valid():
            executor = Compiler()
            code = form.cleaned_data['code']

            executor.set_code(code)
            
            execution_result = executor.execute()

            executor.delete_code_file()

            return HttpResponse("Worked!")
            
        else:
            return HttpResponse("Cannot sanitize form data")
    else:
        form = forms.CodeExecutorForm()
        template_data['form'] = form
        return render(request, 'test-compiler.html', template_data)
