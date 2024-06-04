import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())

