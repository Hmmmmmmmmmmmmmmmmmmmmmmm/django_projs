from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def main_func(request):
    return HttpResponse("Main")


def index(request):
    return HttpResponse("This works!!!!!")
    # instantiating an object of HttpResponse class
    #we can send a html but we are sending a simple string
    #now to tell django when to call this index function
    #we have to mention it in the urls.py file

# now making functions for each months:

# def january(request):
#     return HttpResponse("January Challenge: Set clear goals and build a daily routine.")

# def february(request):
#     return HttpResponse("February Challenge: Focus on consistency and healthy habits.")

# def march(request):
#     return HttpResponse("March Challenge: Learn a new skill or improve an existing one.")

# def april(request):
#     return HttpResponse("April Challenge: Improve time management and productivity.")

# def may(request):
#     return HttpResponse("May Challenge: Prioritize physical fitness and mental well-being.")

# def june(request):
#     return HttpResponse("June Challenge: Strengthen professional or academic skills.")

# def july(request):
#     return HttpResponse("July Challenge: Enhance creativity and explore new ideas.")

# def august(request):
#     return HttpResponse("August Challenge: Improve communication and collaboration.")

# def september(request):
#     return HttpResponse("September Challenge: Focus on learning and personal growth.")

# def october(request):
#     return HttpResponse("October Challenge: Practice discipline and long-term planning.")

# def november(request):
#     return HttpResponse("November Challenge: Cultivate gratitude and mindfulness.")

# def december(request):
#     return HttpResponse("December Challenge: Reflect on achievements and plan for the next year.")

# a better alternative:
# from django.http import HttpResponse

#data:
challenges = {
        'january': 'Set clear goals and build a daily routine.',
        'february': 'Focus on consistency and healthy habits.',
        'march': 'Learn a new skill or improve an existing one.',
        'april': 'Improve time management and productivity.',
        'may': 'Prioritize physical fitness and mental well-being.',
        'june': 'Strengthen professional or academic skills.',
        'july': 'Enhance creativity and explore new ideas.',
        'august': 'Improve communication and collaboration.',
        'september': 'Focus on learning and personal growth.',
        'october': 'Practice discipline and long-term planning.',
        'november': 'Cultivate gratitude and mindfulness.',
        'december': 'Reflect on achievements and plan for the next year.',
    }
    

def month_view(request, month):
    month = month.lower();
    if month not in challenges:
        return HttpResponse("Which month is this??", status =404 )
    return HttpResponse(f"{month.capitalize()} Challenge: {challenges[month]}")


# we basically made it a dynamic single url

def monthly_view_number_based(request,month):
    months = list(challenges.keys())
    if month>len(months) or month<1:
        return HttpResponse(f"Since when is there a {month}'th month eh?",status=404)
    redirected_month=months[month-1]
    return HttpResponseRedirect(''+redirected_month)