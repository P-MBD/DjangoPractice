from django.shortcuts import render, get_object_or_404	
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView, DetailView, FormView
from .models import Post
from .forms import PostForm
# Create your views here.
def indexView (request):
    return render(request, "index.html")

class IndexView(TemplateView):
    template_name= 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context

class RedirectToMaktab(RedirectView):
    url= 'https://maktabkhooneh.com'
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

class PostList(ListView):
   #queryset = Post.objects.all()
    #model = Post
    context_object_name = "posts"
    def get_queryset(self):
        posts = Post.objects.filter(status= False)
        return posts

class PostDetailsView(DetailView):
     model = Post

class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

