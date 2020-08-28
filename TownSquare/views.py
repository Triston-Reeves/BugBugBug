from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from TownSquare.models import Ticket, MyUser
from django.contrib.auth.decorators import login_required
from TownSquare.forms import LoginForm, Ticket, MyUser



@login_required
def index_view(request):
    tickets = models.Ticket.objects.all()
    new_tickets =  tickets.filter(status="New").order_by("-date")
    in_progress_tickets = tickets.filter(status="In Progress")
    done_tickets = tickets.filter(status="Done")
    invalid_tickets = tickets.filter(status="Invalid")
    return render(request, "index.html", {"new_tickets": new_tickets, "in_progress_tickets": in_progress_tickets, "done_tickets": done_tickets, "invalid_tickets": invalid_tickets})

@login_required
def ticket_detail_view(request, ticket_id):
    my_ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, "ticket_detail.html")

@login_required
def add_ticket(request):
    if request.method == "POST":
        form = Ticket(request.POST)
        if form.is_valid():
            Data = form.cleaned_data
            Ticket.objects.create(
                title = data.get("title"),
                description = data.get("description"),
                ticket_author = request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = Ticket()
    return render(request, "index.html", {"form": forms})


def user_detail_view(request, user_id):
    my_user = User.objects.filter(id=user_id).first()
    return render(request, "user_detail.html")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
                
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))