from datetime import datetime
import random
import pytest
from faker import Faker
fake = Faker('vi_VN')
def base_voucher_data(voucher_type=None):
    timestamp = datetime.now().strftime("%d%H%M%S%f")
    return {
        "name": f"Novelite{timestamp}",
        "images": [
            "https://images.steamusercontent.com/ugc/5985917399670227255/DBD1A43CEE20A022527DCE769B5706746F006355/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true"
        ],
        "thumbnail": "https://img.itch.zone/aW1nLzE1MDI4MjM2LnBuZw==/original/qh2GMh.png",
        "category": "travel",
        "title": fake.word(),
        "startDate": 1774976400000,
        "endDate": 1780333199999,
        "pointExchange": 1000,
        "apply": "all",
        "description": fake.sentence(nb_words=20),
        "hashtag": fake.word(),
        "codePrefix": "",
        "originPrice": 1000,
        "point": None,
        "percentAccumulate": None,
        "getCodeMethod": "random",
        "zone": "Toàn quốc",
        "applytoProductIds": [],
        "applytoCategoryIds": [],
        "lockApplyStores": False,
        "discountBillMin": 1000,
        "showOutHomePage": False,
        "applySaleTypes": "all",
        "forSale": False,
        "codeExpiredDuration": 31536000,
    }
def build_discount_voucher_data():
    payload = base_voucher_data()
    payload.update({
        "type": "discount",
        "typeValue": "percentage",
        "discountPercent": random.choice([10, 20, 30]),
        "discount": None,
        "pointMax": None,
        "discountMax": None,
    })
    return payload
def build_discount_constant_voucher_data():
    discountAmount = random.choice([10000, 20000, 30000])
    payload = base_voucher_data()
    payload.update({
        "type": "discount",
        "typeValue": "constant",
        "discount": discountAmount,
        "discountPercent": None,
        "pointMax": None,
        "discountMax": discountAmount,
    })
    return payload
def build_gift_voucher_data():
    payload = base_voucher_data()
    payload.update({
        "type": "gift_stamp",
        "typeValue": None,
        "discountPercent": None,
        "discount": None,
        "pointMax": None,
        "discountMax": None,
        "stampCount": 2,
        "giftStampProductIds": [1987, 1984, 1985, 1986],
    })
    return payload
def build_cash_multiple_voucher_data():
    max = random.randint(10000, 50000000)
    discountEach = random.randint(1000, max)
    payload = base_voucher_data()
    payload.update({
        "type": "cash_multiple",
        "typeValue": None,
        "discountPercent": None,
        "discount": max,
        "percentAccumulate": None,
        "pointMax": None,
        "discountMax": discountEach,
        "discountPercentBillMax": random.randint(1, 50),
    })
    return payload
def build_voucher_data(vouchertype):
    if vouchertype == "discount_percentage":
        return build_discount_voucher_data()
    elif vouchertype == "discount_constant":
        return build_discount_constant_voucher_data()
    elif vouchertype == "gift":
        return build_gift_voucher_data()
    elif vouchertype == "cash_multiple":
        return build_cash_multiple_voucher_data()
    else:
        raise ValueError(f"Unsupported voucher type: {vouchertype}")   

@pytest.fixture
def voucher_data():
    def _factory(vouchertype):
        return build_voucher_data(vouchertype)
    return _factory