from datetime import date

from django import views
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post


class PostView(views.View):
    success_url = '/'

    def get(self, request, **kwargs):
        post = Post(
            text=request.GET['text'],
            creator=request.user,
            date=date.today()
        )
        post.save()
        return HttpResponseRedirect(self.success_url)


post = PostView.as_view()


class TimelineView(views.generic.TemplateView):
    template_name = 'timeline.html'

    def get_context_data(self, **kwargs):
        context = super(TimelineView, self).get_context_data(**kwargs)
        context['posts'] = (self.request.user.posts.all() |
                            Post.objects.filter(
                                creator__in=self.request.user.contacts.all()
                                ) |
                            Post.objects.filter(
                                creator__in=self.request.user.contacted.all()
                                )).order_by('date')
        context['new_post'] = PostForm()
        return context


timeline = TimelineView.as_view()
