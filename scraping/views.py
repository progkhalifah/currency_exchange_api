from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scraping.models import *
from scraping.serializers import *


#################################### Section of All Scraping ###################################################################

@api_view(['GET'])
def get_all_scraping(request):
    if request.method == "GET":
        try:
            currency_sanaa = CurrencyWebsiteSanaa.objects.all()
            serializer_currency_sanaa = CurrencyWebsiteSanaaSerializer(currency_sanaa, many=True)

            currency_aden = CurrencyWebsiteAden.objects.all()
            serializer_currency_aden = CurrencyWebsiteAdenSerializer(currency_aden, many=True)

            gold = GoldWebsite.objects.all()
            serializer_gold = GoldWebsiteSerializer(gold, many=True)

            response_data = {
                "status": "ok",
                "code": status.HTTP_200_OK,
                "total_sanaa": len(serializer_currency_sanaa.data),
                "total_aden": len(serializer_currency_aden.data),
                "total_gold": len(serializer_gold.data),
                "data_sanaa": serializer_currency_sanaa.data,
                "data_aden": serializer_currency_aden.data,
                "data_gold": serializer_gold.data,
            }
            return Response(response_data, status.HTTP_200_OK, content_type="application/json")
        except Exception as e:
            response_data = {
                "status": "Failed",
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": f"There is something wrong: {str(e)}"
            }
            return Response(response_data, status.HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json")

#################################### END Section of All Scraping ###############################################################


@api_view(['GET'])
def get_all_scraping_sanaa(request):
    if request.method == "GET":
        try:
            currency_sanaa = CurrencyWebsiteSanaa.objects.all()
            serializer_currency_sanaa = CurrencyWebsiteSanaaSerializer(currency_sanaa, many=True)

            response_data = {
                "status": "ok",
                "code": status.HTTP_200_OK,
                "total_sanaa": len(serializer_currency_sanaa.data),
                "data_sanaa": serializer_currency_sanaa.data,
            }
            return Response(response_data, status.HTTP_200_OK, content_type="application/json")
        except Exception as e:
            response_data = {
                "status": "Failed",
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": f"There is something wrong: {str(e)}"
            }
            return Response(response_data, status.HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json")

#################################### END Section of Scraping Sanaa ###############################################################


#################################### Section of Scraping Aden ###################################################################

@api_view(['GET'])
def get_all_scraping_aden(request):
    if request.method == "GET":
        try:
            currency_aden = CurrencyWebsiteAden.objects.all()
            serializer_currency_aden = CurrencyWebsiteAdenSerializer(currency_aden, many=True)

            response_data = {
                "status": "ok",
                "code": status.HTTP_200_OK,
                "total_aden": len(serializer_currency_aden.data),
                "data_aden": serializer_currency_aden.data,
            }
            return Response(response_data, status.HTTP_200_OK, content_type="application/json")
        except Exception as e:
            response_data = {
                "status": "Failed",
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": f"There is something wrong: {str(e)}"
            }
            return Response(response_data, status.HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json")

#################################### END Section of Profile ###############################################################


#################################### Section of Profile ###################################################################

@api_view(['GET'])
def get_all_scraping_gold(request):
    if request.method == "GET":
        try:

            gold = GoldWebsite.objects.all()
            serializer_gold = GoldWebsiteSerializer(gold, many=True)

            response_data = {
                "status": "ok",
                "code": status.HTTP_200_OK,
                "total_gold": len(serializer_gold.data),
                "data_gold": serializer_gold.data,
            }
            return Response(response_data, status.HTTP_200_OK, content_type="application/json")
        except Exception as e:
            response_data = {
                "status": "Failed",
                "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": f"There is something wrong: {str(e)}"
            }
            return Response(response_data, status.HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json")

#################################### END Section of Profile ###############################################################



