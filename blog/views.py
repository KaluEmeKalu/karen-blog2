
from django.shortcuts import render
from . models import Comment

def home_page(request):
   
    comments = Comment.objects.all()
    comm1 = comments[0]

    if request.method == 'POST':
        our_comment = request.POST.get('comment')
        our_user = request.POST.get("username")
        comment_obj = Comment.objects.create(
        comment=our_comment,
        user=our_user
        )
        comments = Comment.objects.all()


        return render(request, 'blog/home_page.html', {'comments': comments,})
    return render(request, 'blog/home_page.html', {'comments': comments}) 

