from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AllowAny, )

@csrf_exempt
@api_view(['GET', 'POST'])
def product_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, context={'request': request}, many=True)
        return Response({'data': serializers.data})
    elif request.method == 'POST':
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = ProductSerializer(product, context={'request': request})
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = ProductSerializer(product, data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Review Stuff
@csrf_exempt
@api_view(['GET', 'POST'])
def review_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewSerializier(reviews, context={'request': request}, many=True)
        return Response({'data': serializers.data})
    elif request.method == 'POST':
        serializers = ReviewSerializier(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getReview(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = ReviewSerializier(review, context={'request': request})
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = ReviewSerializier(review, data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Profile
@csrf_exempt
@api_view(['GET', 'POST'])
def profile_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializers = ProfileSerializer(profile, context={'request': request}, many=True)
        return Response({'data': serializers.data})
    elif request.method == 'POST':
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getProfile(request, pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = ProfileSerializer(profile, context={'request': request})
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)