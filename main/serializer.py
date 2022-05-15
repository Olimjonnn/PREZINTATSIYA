from rest_framework import serializers 
from main.models import *

serializer = serializers.ModelSerializer


class SliderSerializer(serializer):
    class Meta:
        model = Slider
        fields = "__all__"


class CategorySerializer(serializer):
    class Meta:
        model = Category
        fields = "__all__"


class WearsSerializer(serializer):
    class Meta:
        model = Wears
        fields = "__all__"


class WearsProductionSerializer(serializer):
    class Meta:
        model = WearsProduction
        fields = "__all__"


class CartSerializer(serializer):
    class Meta:
        model = Cart
        fields = "__all__"


class WishlistSerializer(serializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


class CashSerializer(serializer):
    class Meta:
        model = Cash
        fields = "__all__"


class BuySerializer(serializer):
    class Meta:
        model = Slider
        fields = "__all__"

class NewsLetterSerializer(serializer):
    class Meta:
        model = NewsLetter
        fields = "__all__"

class InfoSerializer(serializer):
    class Meta:
        model = Info
        fields = "__all__"

