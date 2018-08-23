from django.http import Http404, HttpResponse

from django.shortcuts import redirect, render

from django.views.generic import DetailView, ListView

from .forms import UserForm

from .models import User

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)

        # In real life we'd retrieve this from the session.
        context['name'] = 'Adonis'
        
        return context

class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'

def add(request):

    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():
            # Create and save directly.

            User(
             first_name=form.cleaned_data['first_name'], 
             last_name=form.cleaned_data['last_name'],
             email=form.cleaned_data['email'],
             age=form.cleaned_data['age']).save()
        
            return redirect('users:index')

        else:
            # Render form with errors.
            return render(request, 'users/add.html', { 'form' : form })

    else:
        # If the user sends a GET request...

        context = { 'header' : 'GET', 'form' : UserForm() }

        return render(request, 'users/add.html', context)
