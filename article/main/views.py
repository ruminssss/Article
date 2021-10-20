from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArtForm, CommentForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Art
from .models import Comment

def index(request):
    arts = Art.objects.all()
    return render(request, 'main.html', {'arts':arts})

class UserLogin(LoginView):
    template_name = 'login.html'

class UserLogout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'

class ArtCreateView(CreateView):
    template_name = 'add.html'
    form_class = ArtForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ArtCreateView, self).get_context_data()
        context['arts'] = Art.objects.all()
        return context

def comments(request, pk):
    art = Art.objects.get(pk=pk)
    comments = Comment.objects.filter(art=pk)
    initial = {'art':art.pk}
    form_class = CommentForm
    form = CommentForm(initial=initial)
    if request.method == 'POST':
        c_form = form_class(request.POST)
        c_form.save()
    context = {'arts':art, 'comments':comments, 'form':form}
    return render(request, 'comments.html', context)