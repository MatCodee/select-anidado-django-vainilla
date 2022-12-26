from django.shortcuts import render
from django.views import View
from .forms import formSelect

class HomeView(View):
    def get(self,request):
        context = {}
        template_name = 'home.html'
        
        form = formSelect()
        if form.is_valid():
            pass

        return render(request,template_name,context)




from django.views.generic import TemplateView
from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import formSelect
from .models import Category,Product


class TestView(TemplateView):
    template_name = 'home.html'
    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                print("entro aqui")
                data = []
                for i in Product.objects.filter(category__id=request.POST['id']):
                    data.append({'id': i.id, 'name': i.name})
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            print(str(e))
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario Anidado'
        context['form'] = formSelect()
        return context 