from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from .models import Users, Trips, Role

def logIn(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        user_obj = Users.objects.get(email=email)

        if user_obj:
            if user_obj.password == request.POST.get("password"):
                request.session['user_id'] = user_obj.user_id
                if user_obj.role.name == 'admin':
                    return HttpResponse("<strong>Welcome Admin.</strong>")
                elif user_obj.role.name == 'client':
                    return HttpResponseRedirect("/webTrack/viewName")
                else:
                    return HttpResponse("<strong>Welcome Driver.</strong>")
            else:
                messages.error(request, "Invaild Password.")
                return render(request, "login.html")
        else:
            messages.error(request, "Invaild Email-ID.")
            return render(request, "login.html")
    return render(request, "login.html")

def view_Name(request):
    if request.session.has_key('user_id'):
        return HttpResponse('Client : Session Working.')
    else:
        return render(request, "login.html")

def logOut(request):
    request.session.flush()
    return HttpResponse("<strong>You are logged out.</strong>")


'''
                    r = Role.objects.get(name = 'driver')
                    list_of_drivers = Users.objects.filter(company_id=user_obj.company_id, role='Driver')
                    print list_of_drivers
                    for l in list_of_drivers:
                        user_trips = Trips.objects.values('score').filter(user_id=l.user_id)
                        #print user_trips
                        some_list= []
                        for i in user_trips:
                            some_list.append(type(i['score']))
                        #    print some_list.append((i['score']))

                        print numpy.mean(some_list)

'''



