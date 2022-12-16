1. Add these two lines in the project urls:
path('api/v1/', include('api.urls')),
path('api-auth/', include('rest_framework.urls')),


1. 
* create default router in the api/urls.py

1. Question model: 
* create question serializer
* create question view set
* create question url
* install and add restframework to settings.py "rest_framework"
* test api /api/v1


create a User serializer 
then view set then url (user viewset)

currentUser endpoint

nestedresultserializer