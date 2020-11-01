from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from timeline.forms import PostForm

from .forms import RegisterForm

User = get_user_model()


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_post'] = PostForm()
        context['contacts'] = (User.objects.get(
                                username=self.request.user.username
                            ).contacts.all() | User.objects.get(
                                username=self.request.user.username
                            ).contacted.all()).order_by('username')
        context['invites'] = self.request.user.invited.all()
        return context


home_page = ProfileView.as_view()


class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_post'] = PostForm()
        context['contact'] = User.objects.get(
            username=self.kwargs['username'])
        context['contacts'] = (User.objects.get(
                                username=context['contact'].username
                            ).contacts.all() | User.objects.get(
                                username=context['contact'].username
                            ).contacted.all()).order_by('username')
        return context


contact_page = ContactView.as_view()


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.data['password'])
        user.save()
        return super(RegisterView, self).form_valid(form)


register = RegisterView.as_view()


def invite(request, contact, **kwargs):
    print(request.GET)
    if 'recusar' in request.GET:
        request.user.invited.get(inviter__username=contact).deny()
    else:
        request.user.add_contact(contact)

    return HttpResponseRedirect(reverse('perfil:contact', args=[contact]))
