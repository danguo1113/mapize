from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from django import forms
import crawl_for_lst

class SubmitURLForm(forms.Form):
    url_to_crawl = forms.CharField()

def submit_form(request):
    if request.method == 'POST':
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            # Do stuff
            url_to_crawl = form.cleaned_data['url_to_crawl']
            lst_of_locations = crawl_for_lst.get_lst_of_locations(url_to_crawl)
            context = {'lst_of_locations': lst_of_locations}
            return render_to_response('crawl_result.html',context_instance=RequestContext(request,context))
    else:
        form = SubmitURLForm()
    return render(request, 'submit_url.html',{'form':form,})


def home(request):
    return render_to_response('home.html')
