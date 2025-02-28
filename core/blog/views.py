from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.

# Function Base View 
'''
def indexView(request):
    name = "reyhane"
    context = {"name":name}
    return render(request,"index.html",context)
'''

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context
    
# from django.shortcuts import redirect
# def redirectToMaktab(requedt):
#     return redirect('https://maktabkhooneh.com')

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'


class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    # model = Post
    permission_required = 'blog.view_post'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by=2
    ordering = '-id'
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'