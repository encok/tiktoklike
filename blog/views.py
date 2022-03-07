from django.shortcuts import render


posts = [
    {
        'author': 'Enock',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 27, 2022'
    },
     {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'February 27, 2022'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
