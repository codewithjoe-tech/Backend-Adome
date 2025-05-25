
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination



class PostImageView(APIView):
    def post(self, request):
        serializer = LogoImagesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PostTenantImageView(APIView):
    def post(self, request):
        serializer = TenantImageBucketSerializer(data = request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user, tenant=request.tenant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostTenantChapterVideo(APIView):
    def post(self, request):
        serializer = TenantChapterVideoSerializer(data = request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user, tenant=request.tenant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TenantImageBucketPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class GetTenantImageBucket(APIView):
    def get(self, request, contenttype):
        tenant = request.tenant  # directly from middleware
        queryset = TenantImageBucket.objects.filter(
            tenant=tenant,
            content_type=contenttype
        ).order_by('-created_at')

        paginator = TenantImageBucketPagination()
        paginated_qs = paginator.paginate_queryset(queryset, request)
        serializer = TenantImageBucketSerializer(paginated_qs, many=True , context={
            'request' : request
        })
        return paginator.get_paginated_response(serializer.data)
