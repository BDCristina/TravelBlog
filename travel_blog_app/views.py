from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'travel_blog_app/home.html')

def my_button(request):
    button_text = 'SEE LAST POSTS'
    return render(request, 'travel_blog_app/hero.html', {'button_text': button_text})


