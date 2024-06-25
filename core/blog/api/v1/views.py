from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets
from rest_framework import mixins

'''@api_view(["GET","POST"])
def postList(request):
    if request.method == "GET":
        posts =Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)'''
'''class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request):
       posts = Post.objects.filter(status=True)
       serializer = PostSerializer(posts,many=True)
       return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''

class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

'''@api_view(["GET","PUT", "DELETE"])
def postDetail(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"Detail":"item removed successfully"})'''

'''class PostDetail(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request,id):
        """retriveing the post data"""
        post = get_object_or_404(Post,pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self,request,id):
        """editing the post data"""
        post = get_object_or_404(Post,pk=id)
        serializer = self.serializer_class(post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)'''

'''class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes =[IsAuthenticatedOrReadOnly] 
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)'''

'''class PostDetail(RetrieveDestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
'''
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    @action(methods=["get"], detail=False)
    def get_ok(self, request):
        return Response({'detail':'ok'})
    
class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()