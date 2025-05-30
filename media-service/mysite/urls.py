
from django.contrib import admin
from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload' , PostImageView.as_view()),
    path('upload-video' , PostTenantChapterVideo.as_view()),
    path('upload-tenant' , PostTenantImageView.as_view() ),
    path('get-bucket/<contenttype>' ,GetTenantImageBucket.as_view() )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
