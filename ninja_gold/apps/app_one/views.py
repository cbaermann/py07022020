from django.shortcuts import render, redirect
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    context = {}
    context['gold'] = request.session['gold']
    return render(request, 'app_one/index.html', context)

def process_money(request):
    location = request.POST['location']
    gold = request.session['gold']
    print(request.POST['location'])
    print(request.method)
    if request.method == "POST":
        if location == 'farm':
            gold = random.randint(10,20)
        if location == 'cave':
            gold = random.randint(5,10)
        if location == 'house':
            gold = random.randint(2,5)
        if location == 'casino':
            gold = random.randint(-50,50)

        request.session['gold'] += gold
        
    return redirect('/')

# Create your views here.
