from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import loader
from models import Faction, FactionRegistration
from models import Character
from models import ItemOwned
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/complete/')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


def home_view(request):
    context = {}
    return render(request, "index.html", context)


def stats_view(request):
    context = {}
    return render(request, 'stats.html', context)


def lore_view(request):
    context = {}
    return render(request, 'lore.html', context)


def codex_view(request):
    context = {}
    return render(request, 'codex.html', context)


def factions_view(request):
    factions = Faction.objects.all() # Faction.objects.prefetch_related('ranks').all()
    # faction_data = []
    # for faction in factions:
    #     temp = [rank for rank in faction.ranks.all()]
    #     temp.sort(key=lambda x: x.rank_level)
    #     faction_data.append(dict(faction=faction, description=faction.description, ranks=temp))
    context = {'factions': factions}
    return render(request, 'factions.html', context)


def faction_show(request, faction_id):
    faction = Faction.objects.filter(id=faction_id).first()
    ranklist = [rank for rank in faction.ranks.all()]
    ranklist.sort(key=lambda x: x.rank_level)
    context = {'faction': faction, 'ranks': ranklist}
    return render(request, 'faction_show.html', context)


def characters_view(request):
    characters = Character.objects.all()
    context={'characters': characters}
    return render(request, 'characters.html', context)


def character_show(request, char_id):
    character = Character.objects.filter(id=char_id).first()
    items_owned = ItemOwned.objects.filter(owner=character).all()
    items = [{'item': x.item.name, 'description': x.item.description, 'count': x.count}
             for x in items_owned if x.count > 0]
    registrations = FactionRegistration.objects.filter(character=character).all()
    print registrations
    memberships = [{'rank': x.faction_rank.name, 'faction': x.faction.name} for x in registrations]
    print memberships
    exp_info_dict = exp_info(character.level, character.exp)
    context={'character': character, 'items': items, 'memberships': memberships}
    context.update(exp_info_dict)
    return render(request, 'character_show.html', context)

def guide_view(request):
    context={}
    return render(request, 'guide.html', context)

def skills_view(request):
    context={}
    return render(request, 'skills.html', context)

# Helper functions
def exp_to_next_level(current_level):
    # The exp to level increases by 50 every 5 levels, starting at 50.  Using python's natural integer flooring.
    return ((current_level / 5) + 1) * 50


def exp_percent_for_level(lower, upper, current):
    # Because we are searching for an integerial percent, it is easier to multiply the earned exp by 100 first, so that
    # the result will always be an integer floored positive number.  The assumption is that 'current' will always be
    # greater or equal to 'lower', but less than 'upper'
    exp_range = upper - lower
    exp_earned = 100 * (current - lower)
    exp_percent = exp_earned / exp_range

    # If the percent is 0, return 1 so that a sliver shows up in the views
    if exp_percent == 0:
        return 1
    else:
        return exp_percent


def exp_info(current_level, current_exp):
    lower_exp = 0
    # Sums up the experience needed per level to reach this level to get the total exp needed for the current level.
    for x in xrange(0, current_level):
        lower_exp += exp_to_next_level(x)
    # Adding the exp to level up to the next level gives the total experience needed to reach the next level
    upper_exp = lower_exp + exp_to_next_level(current_level + 1)
    current_exp_percentage = exp_percent_for_level(lower_exp, upper_exp, current_exp)

    return {"lower_exp": lower_exp, "upper_exp": upper_exp, "next_level": current_level + 1,
            "experience_percent": current_exp_percentage}
