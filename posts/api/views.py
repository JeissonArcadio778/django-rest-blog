from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(ViewSet):

    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many= True) #return list complete
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        # Validation: 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        


# class PostApiView(APIView):

#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many= True) #return list complete
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         # Validation: 
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
