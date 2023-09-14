import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import consts


class ConvertApiView(APIView):
    def get(self, request):
        params_dict = {}
        for param_name in consts.QUERY_PARAMS:
            param_value = request.query_params.get(param_name)
            if not param_value:
                return Response(
                    {
                        consts.RESPONSE_STATUS: consts.STATUS_ERROR,
                        consts.RESPONSE_DETAIL: consts.QUERY_ERROR_DETAIL
                        % param_name.upper(),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            params_dict[param_name] = param_value
        all_symbols = requests.get(consts.API_CURRENCIES_ENDPOINT).json()
        for symbol_param in consts.QUERY_PARAMS[:-1]:
            if (
                params_dict[symbol_param].upper()
                not in all_symbols[consts.CURRENCY_RESPONCE_SYMBOLS]
            ):
                return Response(
                    {
                        consts.RESPONSE_STATUS: consts.STATUS_ERROR,
                        consts.RESPONSE_DETAIL: consts.CURRENCY_ERROR_DETAIL,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        try:
            request = requests.get(
                consts.API_ENDPOINT, params=params_dict, timeout=consts.API_TIMEOUT
            )
        except requests.exceptions.Timeout:
            return Response(
                {
                    consts.RESPONSE_STATUS: consts.STATUS_ERROR,
                    consts.RESPONSE_DETAIL: consts.TIMEOUT_ERROR_DETAIL,
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        response = request.json()
        if response.get(consts.STATUS_SUCCESS):
            return Response(
                {consts.RESPONSE_RESULT: response.get(consts.RESPONSE_RESULT)},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    consts.RESPONSE_STATUS: consts.STATUS_ERROR,
                    consts.RESPONSE_DETAIL: consts.API_ERROR_DETAIL,
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
