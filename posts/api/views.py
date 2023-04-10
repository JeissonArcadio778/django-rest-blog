from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostModelViewSet(ModelViewSet):

    # Permissions: 
    permission_classes = [IsAdminOrReadOnly] #IsAdminUser # IsAuthenticatedOrReadOnly

    serializer_class = PostSerializer
    
    # los objectos que vamos a usar. 
    queryset = Post.objects.all()
    
    # CRUD created!
    # http_method_names = ['get', 'put']






# class PostViewSet(ViewSet):

#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many= True) #return list complete
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def retrieve(self, request, pk:int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)


#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         # Validation: 
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        

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
        
