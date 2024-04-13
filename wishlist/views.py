from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .models import Wishlist
from django.http import JsonResponse
from .serializer import WishlistSerializer
from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 16

@api_view(['GET'])
def getProductsByWishlist(request):
    try:
        wishlist_items = Wishlist.objects.filter(user_id=request.user)
        paginator = StandardResultsSetPagination()
        wishlist_items_for_page = paginator.paginate_queryset(wishlist_items,request)
        serializer = WishlistSerializer(wishlist_items_for_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Wishlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProductsToWishlist(request):
    try:
        product_id = request.data.get('product')
        product = Product.objects.get(id=product_id)
        likedProduct = Wishlist.objects.filter(product=product, user=request.user)
        if not likedProduct:
            wishlist_item = Wishlist.objects.create(user=request.user, product_id=product_id)
            serializer = WishlistSerializer(wishlist_item)
            # if serializer.is_valid():
                # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Product already exists in the wishlist"})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeProductsToWishlist(request):
    try:
        product_id = request.data.get('product')
        wishlist_item = Wishlist.objects.filter(user_id=request.user, product_id=product_id)
        if wishlist_item:
            wishlist_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Wishlist item does not exist."})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
