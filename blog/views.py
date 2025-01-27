from django.shortcuts import render, get_object_or_404, redirect
import logging
from django.utils import timezone
from blog.models import Post
from .forms import CommentForm
from django.views.decorators.cache import cache_page


logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  logger.debug("this is index views.py")
  logger.debug("Got %d posts", len(posts))
  return render(request, 'blog/index.html', {"posts": posts})

def post_detail(request, slug):
  logger.critical("this is post_detail views.py")
  post = get_object_or_404(Post, slug = slug)


  if request.user.is_active:
    if request.method == 'POST':
      comment_form = CommentForm(request.POST)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        return redirect(request.path_info)

    else:
      comment_form = CommentForm()

  else: comment_form = None

  
  return render(request, 'blog/post-details.html', {"post" : post, "comment_form": comment_form})