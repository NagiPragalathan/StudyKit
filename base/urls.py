from django.urls import path
from .Routes import views,tools,home,Profile

urlpatterns = []

def add_path( paths : list ) -> None:
    for i in paths :
        for j in i:
            urlpatterns.append(j)
        
#ChatRoom Paths

Home = [
    path('', home.home),
]

ChatRoom = [
    path('chat_lobby', views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]

Tools = [
    path("text2sound",tools.TexttoSound),
    path("TexttoHandWritten",tools.TexttoHandWritten),
    path("Dictinary",tools.Dictinary),
    path("KeyWordToAudio",tools.KeyWordToAudio),
    path("KeyWordToText",tools.KeyWordToText),
    path("KeywordToPara",tools.KeywordToPara),
    path("ToolMenu",tools.ToolMenu),
    path("KeyWordToImage",tools.KeyWordToImage),
]
profile = [
    path('login', Profile.index, name='index'),
    path('settings', Profile.settings, name='settings'),
    path('upload', Profile.upload, name='upload'),
    path('follow', Profile.follow, name='follow'),
    path('search', Profile.search, name='search'),
    path('profile/<str:pk>', Profile.profile, name='profile'),
    path('like-post', Profile.like_post, name='like-post'),
    path('signup', Profile.signup, name='signup'),
    path('signin', Profile.signin, name='signin'),
    path('logout', Profile.logout, name='logout'),
]

#Adding all paths to main path

add_path([profile,Home,ChatRoom,Tools])