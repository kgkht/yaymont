from django.shortcuts import render, redirect
from ordering.models import Ordering
from ordering.forms import OrderForm
import datetime

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView    
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontend:home')

    else:
        form = OrderForm()
            
    orders = Ordering.objects.filter(completed=False)
    
    return render(request, 'frontend/index.html', {
        'allorders': orders,
        'form': form,
        } )
        

@login_required(login_url='login')
def updateItem(request, pk):
	obj = Ordering.objects.get(pk=pk)
	obj.completed = True
	obj.save()
	return redirect('frontend:home')
	


@login_required(login_url='login')
def todayLedger(request):
	totalEgg = Ordering.objects.filter(pub_date__date=datetime.date.today() ).filter(completed=True).filter(p_type='E')
	totalSimple = Ordering.objects.filter(pub_date__date=datetime.date.today() ).filter(completed=True).filter(p_type='S')
	DailyList = Ordering.objects.filter(pub_date__date=datetime.date.today() ).filter(completed=True)
	return render(request, 'frontend/daily_report.html', 
	{'dailylist': DailyList,
		'totalEgg': totalEgg,
		'totalSimple': totalSimple,
	})


class ItemDelete(DeleteView):
	model = Ordering
	success_url = reverse_lazy('frontend:home')



class ItemUpdate(UpdateView):
	model = Ordering
	fields = ['name','phone', 'p_type', 'p_count', 'completed']
	success_url = reverse_lazy('frontend:home')
	template_name_suffix = '_update_form'
	
