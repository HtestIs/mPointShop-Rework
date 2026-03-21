from data.fake_location import fake_old_location


def build_store_data(base,**overrides):
    data = base.copy()
    data.update(overrides)
    return data
def build_location_data(base, case):
    if case == "missing_city":
        change = fake_old_location(exclude_city=base["city_old"],exclude_district=None)
        return build_store_data(base, **change)
    elif case == "missing_district":
        change = fake_old_location(exclude_district=base["district_old"])
        return build_store_data(base, **change)