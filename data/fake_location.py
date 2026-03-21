import random

location_data = {
    "T.P Hà Nội":{
        "Quận Ba Đình": ["Phường Phúc Xá", "Phường Trúc Bạch", "Phường Vĩnh Phúc"],
        "Quận Hoàn Kiếm": ["Phường Hàng Bài", "Phường Hàng Bạc", "Phường Hàng Gai"],
        "Quận Tây Hồ": ["Phường Bưởi", "Phường Thụy Khuê", "Phường Yên Phụ"]
    },
    "T.P Hồ Chí Minh":{

        "Quận 1": ["Phường Bến Nghé", "Phường Bến Thành", "Phường Cô Giang"],
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
        "Phú Hoà Đông",
        "Thường Tân"
    ]
    }
def fake_old_location(exclude_city=None,exclude_district=None):
    cities = list(location_data.keys())
    if exclude_city in cities:
        cities = [c for c in cities if c != exclude_city]
    if not cities:
        raise Exception("No cities available to choose from.")
    city = random.choice(cities)
    districts = list(location_data[city].keys())
    if exclude_district in districts:
        districts = [d for d in location_data[city].keys() if d != exclude_district]
    else:
        districts = list(location_data[city].keys())
    district = random.choice(districts)
    ward = random.choice(location_data[city][district])
    return {
    "city_old": city,
    "district_old": district,
    "ward_old": ward
}
def fake_new_location(exclude_city=None):
    cities = list(location_new_data.keys())
    if exclude_city in cities:
        cities = [c for c in cities if c != exclude_city]
    if not cities:
        raise Exception("No cities available to choose from.")
    city = random.choice(cities)
    ward = random.choice(location_new_data[city])
    return {
    "city_new": city,
    "ward_new": ward
}