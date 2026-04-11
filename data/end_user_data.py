from datetime import datetime
import random
import pytest

from data.data_generator import generate_random_phone_number

@pytest.fixture
def user_data():
    return{
        "phone_number": generate_random_phone_number(),
        "password": "111020"
    }