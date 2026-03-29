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
    timestamp = datetime.now().strftime("%d%H%M%S%f")
    password = "Abc@1234"
    return {"name": fake.company(), 
     "username": (fake.user_name()+timestamp)[:20],
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
     "password": password, 
     "confirm_password": password, 
     "commission": fake.random_int(min=1, max=100),
     "min_wallet": "1000000", 
     "transfer_limit": fake.random_int(min=1000000, max=10000000),
     "point_rate": fake.random_number(digits=2),
     "image_path": ICON_AUTO_PATH
     }
#holy f, are you reading my mind, this is exactly the data I want to generate for store registration, you are a genius, I am amazed, I will use this for my test_register_new_store test case, thank you so much
@pytest.fixture
def store_api_data():
    timestamp = datetime.now().strftime("%d%H%M%S%f")
    return{
        "address": f"{fake.building_number()} {fake.street_name()}, Phường {fake.first_name()}, {fake.city()}",
        "bankAccount": fake.aba(),
        "bankId": None,
        "businessLicenseImage": "",
        "district": "271",
        "image": "https://s3.mpoint.vn/mpointshop/shioriNovellaHololiveAnd1MoreDrawnByDinoDinoartforameD4B708F6Ce27Caa33Fd7D568F81671Be_691d047c00609a3115b828f8b64752ab.jpg",
        "lat": "25.123123123",
        "lng": "105.123123123123",
        "nameStore": fake.company(),
        "newProvinceId": 1,
        "newWardId": 2,
        "password": "Abc@1234",
        "percent": 50,
        "phoneStore": fake.numerify(text='09########'),
        "pointTransferLimit": 1000000,
        "province": "1",
        "saleCommissionOffline": 5,
        "storeOwnerBusinessCompanySeId": None,
        "storeOwnerName": fake.name(),
        "storeOwnerPhone": fake.numerify(text='09########'),
        "username": ("API"+timestamp)[:20],
        "walletBalanceMin": 1000000,
        "ward": "9619",
        "whitelistSerials": []
    }