from .models import Post

def context_processor(request):
    all_post = Post.objects.all()
    return {'posts': all_post}