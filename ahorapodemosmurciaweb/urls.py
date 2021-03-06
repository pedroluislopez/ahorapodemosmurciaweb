from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ahorapodemosmurciaweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('web.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
