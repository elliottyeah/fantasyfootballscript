from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from players.models import Player
from forms import  SelecterForm
from forms import ContactForm
from django.template.loader import get_template
from django.core.mail import send_mail
from django.template import Context

def thanks(request):
    return render_to_response('home/thanks.html', context_instance=RequestContext(request))

def index(request):
    return render_to_response('home/home.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('home/about.html', context_instance=RequestContext(request))

#def contact(request):
#    return render_to_response('home/contact.html', context_instance=RequestContext(request))

def find_player(request):
    if request.method == "POST":
        f = SelecterForm(request.POST)
        if f.is_valid():
            pos = f.cleaned_data['position']
            cash = f.cleaned_data['cash']
            players = Player.objects.filter(player_position = pos , buy_value__lte = cash).exclude(news__icontains= 'injury - E').exclude(news__icontains = 'injury - U').exclude(news__icontains = 'Joined ').exclude(news__icontains = 'Transferred').exclude(news__icontains = 'Loaned').exclude(news__icontains = 'Left club')[:5]
            return render(request, 'home/player_results.html', {'players':players})
    else:
        f = SelecterForm()
    return render(request, 'home/player_form.html', {'form': f})


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            # Email the profile with the
            # contact information
            template = get_template('home/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
            email_subject = "New contact form submission"
            email_from = "FPL Scout" +'<info@fantasypremierleaguescout.com>'
            email_to = ['elliott@submarineconsulting.com','info@fantasypremierleaguescout.com' ]
            send_mail( email_subject, content, email_from, email_to )
            return render(request, 'home/thanks.html')

    return render(request, 'home/contact.html', {'form': form_class,})

def test(request):
    return render_to_response('home/home_test.html', context_instance=RequestContext(request))


"""
contact working but not sending

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            # Email the profile with the
            # contact information
            template = get_template('home/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage("New contact form submission",
                content,"Your website" +'<elliott@submarineconsulting.com>',
                ['elliott@submarineconsulting.com'],headers = {'Reply-To': contact_email })
            email.send()
            return render(request, 'home/thanks.html')








def test(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            # Email the profile with the
            # contact information
            template = get_template('home/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage("New contact form submission",
                content,"Your website" +'<elliott@submarine.com>',
                ['elliott@submarineconsulting.com'],headers = {'Reply-To': contact_email })
            email.send()
            return render(request, 'home/thanks.html')

    return render(request, 'home/contact_test.html', {'form': form_class,})
"""

################# backup
"""

def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))


def form_test(request):
    players = Player.objects.filter(player_position= "Defender" , buy_value__lte= 10)[:5]
    return render(request, 'home/form_test.html', {'players':players})


def find_player(request):
    if request.method == "POST":
        f = SelecterForm(request.POST)
        if f.is_valid():
            pos = f.cleaned_data['position']
            cash = f.cleaned_data['cash']
            return redirect(reverse(form_test))
    else:
        f = SelecterForm()
    return render(request, 'home/player_form.html', {'form': f})
"""

########################### below the line didnt work
"""
def filter_test(request):
    players = SelecterForm(request.POST)

    if request.method == 'POST':
        if players.is_valid():
            players = Player.objects.filter(player_position= "Defender" , buy_value__lte= 10)[:5]
    return render(request, 'home/form_test.html', {'players':players})



def player_list(request,pos,cash):
    pos_dict = {'df':"Defender"}
    players = Player.objects.filter(player_position=pos_dict[pos] , buy_value__lte=float(cash))[:5]
    return render(request, 'home/player_list.html', {'players': players})

def find_player_notworking(request):
    if request.method == "POST":
        f = SelecterForm(request.POST)
        if f.is_valid():
            pos = f.cleaned_data['position']
            cash = f.cleaned_data['cash']
            players = Player.objects.filter(player_position= pos , buy_value__lte= cash)[:5]
    else:
        f = SelecterForm()
    return render(request, 'home/player_form.html', {'form': f})
"""