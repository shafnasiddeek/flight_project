from django.shortcuts import render,redirect
from .forms import RouteForm, NodeSearchForm
from .models import Airport, Route
from collections import deque
def home_view(request):
    return render(request, 'home.html')

# This view handles the "Add Route" page

def add_route_view(request):
    form = RouteForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('add_route') 
         # For GET requests (when first opening the page), render the form template 
    return render(request, 'add_route.html', {'form': form})



def nth_node_view(request):
    result = None
    form = NodeSearchForm(request.GET or None)
    if form.is_valid():
        from_code = form.cleaned_data['from_airport']
        direction = form.cleaned_data['direction']
        n = form.cleaned_data['n']
        try:
            current_airport = Airport.objects.get(code=from_code)
            for _ in range(n):
                route = Route.objects.get(from_airport=current_airport, position=direction)
                current_airport = route.to_airport
            result = current_airport
        except:
            result = "Not Found"
    return render(request, 'nth_node.html', {'form': form, 'result': result})

def longest_route_view(request):
    route = Route.objects.order_by('-duration').first()
    return render(request, 'longest_route.html', {'route': route})

def shortest_path_view(request):
    result = None
    if request.GET.get('from') and request.GET.get('to'):
        from_code = request.GET['from']
        to_code = request.GET['to']
        visited = set()
        queue = deque([(Airport.objects.get(code=from_code), 0)])
        while queue:
            current_airport, total_duration = queue.popleft()
            if current_airport.code == to_code:
                result = total_duration
                break
            visited.add(current_airport)
            for route in Route.objects.filter(from_airport=current_airport):
                if route.to_airport not in visited:
                    queue.append((route.to_airport, total_duration + route.duration))
    return render(request, 'shortest_path.html', {'result': result})


# Create your views here.
