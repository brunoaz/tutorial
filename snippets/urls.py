from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
	url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

	url(r'^$', views.api_root),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),

	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Configura o uso do sufixo no request do servico rest.
urlpatterns = format_suffix_patterns(urlpatterns) 