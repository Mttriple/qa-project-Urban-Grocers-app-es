import sender_stand_request
import data


def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body


def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body.copy())
    assert kit_response.status_code == 201


# Prueba 1
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")


# Prueba 2
def test_create_kit_511_letter_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Prueba_5
def test_create_kit_special_letter_in_kit_name_get_success_response():
    positive_assert("\"№%@\",")


# Prueba_6
def test_create_kit_spaces_in_kit_name_get_success_response():
    positive_assert(" A Aaa ")


# Prueba_7
def test_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert("123")


def negative_assert_symbol(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400


# Prueba_3
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_symbol("")


# Prueba_4
def test_create_kit_512_letter_in_kit_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def negative_assert_no_kit_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400


# Prueba_8
def test_create_kit_no_kit_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_kit_name(kit_body)


# Prueba_9
def test_create_kit_number_type_kit_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
