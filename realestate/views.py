from django.shortcuts import redirect, render
from .models import Cards, Agent
from .form import Create_Card_Form
from django.contrib.auth.decorators import login_required

# rents = [
#     {"id":0, "name":"Duplex", "rooms":5},
#     {"id":1, "name":"Bungalow", "rooms":12},
#     {"id":2, "name":"self contain", "rooms":1},
# ]




# Create your views here.
def home(request):
    cardlist = Cards.objects.all()
    context= {'card': cardlist}
    return render(request, 'realestate/home.html', context)


@login_required
def about(request):
    return render(request, 'realestate/about.html')

@login_required
def agent_list(request):
    query_agent_list = Agent.objects.all()
    context= {'agent': query_agent_list}
    return render(request, 'realestate/agent_list.html', context)


def list_detail(request, pk):
    list_id = Cards.objects.get(id=pk)
    context={'details': list_id}
    return render(request, 'realestate/list_details.html',context)


def create_form(request):
    form = Create_Card_Form()
    if request.method == 'POST':
        form = Create_Card_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'cardform': form}
    return render(request, 'realestate/cardform.html', context)

def update_form(request, pk):
    list_id = Cards.objects.get(id=pk)
    form = Create_Card_Form(instance=list_id)
    if request.method == 'POST':
        form = Create_Card_Form(request.POST, instance=list_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'cardform': form}
    return render(request, 'realestate/updateform.html', context)



def delete(request, pk):
    list_id = Cards.objects.get(id=pk)
    list_id.delete()
    return redirect('/')
