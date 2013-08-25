from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from django import forms
import crawl_for_lst

class SubmitURLForm(forms.Form):
    url_to_crawl = forms.CharField()

def create_location_lst(lst_of_locations):
    location_lst_formatted = []
    for tup in enumerate(lst_of_locations):
        try:
            key = tup[1]
            curr_location_lst = []
            loc_data = crawl_for_lst.get_map_for_location(key)
            curr_location_lst.append(key.encode('utf-8'))
            curr_location_lst.append(loc_data['lat'])
            curr_location_lst.append(loc_data['lng'])
            curr_location_lst.append(tup[0])
            location_lst_formatted.append(curr_location_lst)
        except KeyError:
            print 'No data'
    return location_lst_formatted

def submit_form(request):
    if request.method == 'POST':
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            # Do stuff
            context = {'unknown_url':False}
            url_to_crawl = form.cleaned_data['url_to_crawl']
            try:
                lst_of_locations = crawl_for_lst.get_lst_of_locations(url_to_crawl)
            except ValueError, SyntaxError:
                context['unknown_url'] = True
                return render_to_response('crawl_result.html',context_instance=RequestContext(request,context))
            location_lst_formatted = create_location_lst(lst_of_locations)
            print location_lst_formatted
            context = {'location_lst_formatted':location_lst_formatted}
            return render_to_response('crawl_result.html',context_instance=RequestContext(request,context))
    else:
        form = SubmitURLForm()
    return render(request, 'submit_url.html',{'form':form,})


def home(request):
    return render_to_response('home.html')
