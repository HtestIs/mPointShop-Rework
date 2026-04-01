from datetime import datetime

import pytest
from faker import Faker
fake = Faker('vi_VN')
@pytest.fixture
def voucher_data():
    timestamp = datetime.now().strftime("%d%H%M%S%f")
    return {
    "name": f"Novelite{timestamp}",
    "images": ["https://images.steamusercontent.com/ugc/5985917399670227255/DBD1A43CEE20A022527DCE769B5706746F006355/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true"],
    "thumbnail": "https://img.itch.zone/aW1nLzE1MDI4MjM2LnBuZw==/original/qh2GMh.png",
    "category": "travel",
    "title": "123",
    "startDate": 1774976400000,
    "endDate": 1780333199999,
    "pointExchange": 1000,
    "discountPercent": 20,
    "discount": None,
    "point": None,
    "percentAccumulate": None,
    "pointMax": None,
    "apply": "all",
    "description": fake.sentence(nb_words=50),
    "hashtag": "as",
    "codePrefix": "",
    "originPrice": 1000,
    "getCodeMethod": "random",
    "zone": "Toàn quốc",
    "applytoProductIds": [],
    "applytoCategoryIds": [],
    "lockApplyStores": False,
    "discountBillMin": 1000,
    "showOutHomePage": False,
    "type": "discount",
    "typeValue": "percentage",
    "discountMax": 100000,
    "applySaleTypes": "all",
    "forSale": False,
    "codeExpiredDuration": 31536000
}