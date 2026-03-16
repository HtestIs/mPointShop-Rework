import random

location_data = {
    "Hà Nội":{
        "Ba Đình": ["Phúc Xá", "Trúc Bạch", "Vĩnh Phúc"],
        "Hoàn Kiếm": ["Chương Dương", "Hàng Bạc", "Hàng Gai"],
        "Tây Hồ": ["Bưởi", "Thụy Khuê", "Tây Hồ"]
    },
    "Hồ Chí Minh":{
        "Quận 1": ["Bến Nghé", "Bến Thành", "Cô Giang"],
        "Quận 3": ["Phường 01", "Phường 02", "Phường 03"],
        "Quận 5": ["Phường 01", "Phường 02", "Phường 03"]
    }
}

location_new_data = {
    "Hà Nội":
    [
        "Đống Đa",
        "Ba Đình",
        "Hoàn Kiếm",
        "Tây Hồ",
        "Cầu Giấy",
        "Thanh Xuân"
    ],
    "Hồ Chí Minh":
    [
        "Thanh An",
        "Phú Thạnh",
        "Tân Phú",
        "An Nhơn Tây",
        "Phú Hòa Đông",
        "Thường Tân"
    ]
    }
def fake_old_location():
    city = random.choice(list(location_data.keys()))
    district = random.choice(list(location_data[city].keys()))
    ward = random.choice(location_data[city][district])
    return ward, district, city
def fake_new_location():
    city = random.choice(list(location_new_data.keys()))
    ward = random.choice(location_new_data[city])
    return city, ward