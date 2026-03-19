def build_store_data(base,**overrides):
    data = base.copy()
    data.update(overrides)
    return data