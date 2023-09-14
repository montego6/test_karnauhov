FROM = 'from'
TO = 'to'
AMOUNT = 'amount'
QUERY_PARAMS = (FROM, TO, AMOUNT)

STATUS_ERROR = 'error'
STATUS_SUCCESS = 'success'
QUERY_ERROR_DETAIL = 'value for parameter %s should be provided'
API_ERROR_DETAIL = 'some problem with outer api service'
CURRENCY_ERROR_DETAIL = 'you currency is not supported or misspelled'
TIMEOUT_ERROR_DETAIL = 'timelimit for outer service exceeded'

RESPONSE_STATUS = 'status'
RESPONSE_DETAIL = 'detail'
RESPONSE_RESULT = 'result'

API_ENDPOINT='https://api.exchangerate.host/convert'
API_CURRENCIES_ENDPOINT = 'https://api.exchangerate.host/symbols'
API_TIMEOUT = 0.5

CURRENCY_RESPONCE_SYMBOLS = 'symbols'