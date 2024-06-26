from rest_framework import serializers

from scraping.models import *


class CurrencyWebsiteSanaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyWebsiteSanaa
        fields = "__all__"


# end of user


# start Color
class CurrencyWebsiteAdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyWebsiteAden
        fields = "__all__"


# start Size
class GoldWebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldWebsite
        fields = "__all__"
