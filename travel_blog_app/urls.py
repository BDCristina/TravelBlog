from django.urls import path
from travel_blog_app.views import home_view, my_button


app_name = 'travel_blog_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('my_button/', my_button, name='my_button'),

]