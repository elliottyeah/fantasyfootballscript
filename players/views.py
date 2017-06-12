from django.shortcuts import render_to_response
import simplejson
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the players index.")


"""
def player_return_view(request, position, value):
    pos_dict = {'gk':'Goalkeeper','df':'Defender', 'md':'Midfielder', 'fw':'Forward'}

    try:
        players = Player.objects.filter(player_position=pos_dict['position'] , buy_value__lte=float(value)).order_by(('expected').desc())[:5]
    except:
        raise Http404
    if request.is_ajax():
        return player_return_view_ajax(request, position, value)
    return
"""
def player_table(request):
    xhr = request.GET.has_key('xhr')
    response_dict = {}
    pos = request.POST.get('position', False)
    cash = request.POST.get('cash', False)
    pos_dict = {'gk':'Goalkeeper','df':'Defender', 'md':'Midfielder', 'fw':'Forward'}
    response_dict.update({'cash': cash, 'pos': pos_dict[pos]})
    if xhr:
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    return render_to_response('weblog/ajax_example.html', response_dict)
