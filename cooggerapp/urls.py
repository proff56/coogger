from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import os
from .views import home
from .views import signup_or_login
from .views import detail
from .views import users
from .views import topics
from .views import tools
from .views import controls
from .views import explorer
from .views import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns = [
    url(r'^$', home.home,name = "home"),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r"^signup$",signup_or_login.mysignup,name = "sign_up"),
    url(r"^signup-author$",signup_or_login.signup_author,name = "signup_author"),
    url(r"^login$",signup_or_login.mylogin,name = "login"),
    url(r"^logout/$",signup_or_login.mylogout,name = "logout"),

    url(r'^topic/(?P<topic>.*)',topics.topic),
    url(r'^stars/(?P<post_id>[0-9].*)/(?P<stars_id>[0-9])$',detail.stars),

    url(r'^robots.txt$',tools.seo),
    url(r'^sitemab.xml$',tools.seo),

    url(r'^user-upload-pp$',users.upload_pp,name="user_upload_pp"),

    url(r'^create/$',controls.create,name="create"),
    url(r'^(change/(?P<content_id>.*))',controls.change,name="change"),
    url(r'^(delete/(?P<content_id>.*))',controls.delete,name="delete"),
    url(r'^chosesub/(?P<value>.*)',controls.chose_subcategory),
    url(r'^chosecat2/(?P<value>.*)',controls.chose_category2),
    url(r'^chosenone/$',controls.chosenone),

    url(r'^(?P<blog_path>@.*/(?P<utopic>.*)/(?P<path>.*))', detail.main_detail,name = "blogs"),
    url(r'^@(?P<username>.*)/(?P<utopic>.*)', users.u_topic,name = "u-topic"),
    url(r'^@(?P<username>.*)', users.user,name = "user"),

    url(r'^tags/(?P<hashtag>.*)',explorer.hashtag,name = "hashtag"),
    url(r'^list/(?P<list>.*)',explorer.list,name = "list"),

    url(r'^search',home.search,name = "search"),

    url(r'^comment/(?P<content_path>.*)$',detail.comment,name = "comment"),

    url(r"^settings/profile$",settings.profile),
    url(r"^settings/$",settings.profile),
    url(r"^settings/account$",settings.account),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
