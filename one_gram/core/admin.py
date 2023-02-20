from django.contrib import admin
from .models import Profile , Post ,Liked_Post , FollowersCount

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Liked_Post)
admin.site.register(FollowersCount)