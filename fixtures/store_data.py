import pytest
from faker import Faker
fake = Faker('vi_VN')
@pytest.fixture
def storedata():
    return {"name": fake.company(), 
     "username": fake.user_name(), 
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
     "image_path": "C:\Work\mPointShop_rework\assets\icon_auto.png"
     }
#holy f, are you reading my mind, this is exactly the data I want to generate for store registration, you are a genius, I am amazed, I will use this for my test_register_new_store test case, thank you so much