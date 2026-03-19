from datetime import datetime

import pytest
from faker import Faker
from config.paths import ICON_AUTO_PATH
from data.fake_location import fake_old_location, fake_new_location
fake = Faker('vi_VN')
@pytest.fixture
def storedata():
    old_location = fake_old_location()
    new_location = fake_new_location()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return {"name": fake.company(), 
     "username": fake.user_name()+timestamp,
     "city_old": old_location["city_old"],
     "district_old": old_location["district_old"],
     "ward_old": old_location["ward_old"],
     "city_new": new_location["city_new"],
     "ward_new": new_location["ward_new"],
     "address": fake.address(),
     "gps": "9.814872168201843/105.61238136803532", 
     "manager_name": fake.name(), 
     "manager_phone": fake.phone_number(), 
     "customer_service_phone": fake.phone_number(), 
     "sale_code": "1", 
     "password": "Abc@1234", 
     "confirm_password": "Abc@1234", 
     "commission": fake.random_int(min=1, max=100),
     "min_wallet": "1000000", 
     "transfer_limit": fake.random_int(min=1000000, max=10000000),
     "point_rate": fake.random_number(digits=2),
     "image_path": ICON_AUTO_PATH
     }
#holy f, are you reading my mind, this is exactly the data I want to generate for store registration, you are a genius, I am amazed, I will use this for my test_register_new_store test case, thank you so much