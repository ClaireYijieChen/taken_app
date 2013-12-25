from django.conf.urls import patterns, include, url


urlpatterns = patterns('notes.views',
    # Examples:
    # url(r'^$', 'noteworthy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^submit_note$', 'createNewNote'),
    url(r'^(?P<note_id>\d+)/$', 'note_info'),
    url(r'^add$', 'add_note'),
    url(r'^all/$', 'all_notes'),
    url(r'^$', 'all_notes'),
)