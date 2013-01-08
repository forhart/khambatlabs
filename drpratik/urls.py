from django.conf.urls import patterns, include, url
from django.views.generic import list_detail

from drpratik.khambatlabs.models import Patient

patient_info = {
    'queryset':Patient.objects.all(),
}


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drpratik.views.home', name='home'),
    # url(r'^drpratik/', include('drpratik.foo.urls')),
    (r'^patients/$',list_detail.object_list,patient_info),                   
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
