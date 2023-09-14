import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from main import consts

client = APIClient()


@pytest.mark.parametrize(
    "from_p,to_p,amount_p",
    [("usd", "rub", 1), ("rub", "usd", 1000), ("usd", "eur", 1.5)],
)
def test_convert_api_success_view(from_p, to_p, amount_p):
    response = client.get(
        reverse("api-convert"),
        {consts.FROM: from_p, consts.TO: to_p, consts.AMOUNT: amount_p},
    )
    assert response.status_code == 200
    assert consts.RESPONSE_RESULT in response.data
    assert isinstance(response.data.get(consts.RESPONSE_RESULT), float)
    assert response.data.get(consts.RESPONSE_RESULT) > 0


@pytest.mark.parametrize(
    "query_params,code,detail",
    [
        (
            {consts.FROM: "usd", consts.AMOUNT: 1},
            400,
            consts.QUERY_ERROR_DETAIL % consts.TO.upper(),
        ),
        (
            {consts.TO: "usd", consts.AMOUNT: 1},
            400,
            consts.QUERY_ERROR_DETAIL % consts.FROM.upper(),
        ),
        ({consts.AMOUNT: 1}, 400, consts.QUERY_ERROR_DETAIL % consts.FROM.upper()),
        (
            {consts.FROM: "usd", consts.TO: "eur"},
            400,
            consts.QUERY_ERROR_DETAIL % consts.AMOUNT.upper(),
        ),
        ({}, 400, consts.QUERY_ERROR_DETAIL % consts.FROM.upper()),
        (
            {consts.FROM: "abreg", consts.TO: "usd", consts.AMOUNT: 1},
            400,
            consts.CURRENCY_ERROR_DETAIL,
        ),
        (
            {consts.FROM: "eur", consts.TO: "zx1", consts.AMOUNT: 1},
            400,
            consts.CURRENCY_ERROR_DETAIL,
        ),
    ],
)
def test_convert_api_error_view(query_params, code, detail):
    response = client.get(reverse("api-convert"), query_params)
    assert response.status_code == code
    assert response.data.get(consts.RESPONSE_STATUS) == consts.STATUS_ERROR
    assert consts.RESPONSE_DETAIL in response.data
    assert response.data.get(consts.RESPONSE_DETAIL) == detail
