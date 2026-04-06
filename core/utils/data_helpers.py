def apply_field_value(data, field, value):
    data[field] = value
    if field in ("password", "confirm_password"):
        data["password"] = value
        data["confirm_password"] = value
    return data