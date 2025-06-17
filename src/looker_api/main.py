from datetime import datetime

import looker_sdk

from general_utils.consts import load_env

load_env()
print(datetime.now())
sdk = looker_sdk.init40()  # or init31() for the older v3.1 API
my_user = sdk.me()
validation = sdk.validate_project("default", transport_options={"timeout": 600})
print(datetime.now())
print(validation.errors)
