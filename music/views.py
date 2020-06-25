from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Destination


# Create your views here.


def index(request):
    
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


class DescCreate(CreateView): 
    model = Destination 

  
    fields = [ 
        "name", 
        "img",
		"desc",
		"price",
		"offer"
    ] 

    success_url = '/'
 


class DescUpdate(UpdateView):
    model = Destination
    fields = [ 
        "name", 
        "img",
		"desc",
		"price",
		"offer"
    ] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    success_url = '/'

    

class DescDelete(DeleteView):
    model = Destination

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete'
        return context

    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_url = '/'
    









    


	


