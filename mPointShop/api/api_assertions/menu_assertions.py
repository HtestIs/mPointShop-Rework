def assert_menu_response(body: dict):
    assert "data" in body, "Response should contain 'data' field"
    assert isinstance(body["data"], list), "'data' field should be a list"
    for item in body["data"]:
        assert "id" in item, "Each menu item should contain 'id'"
        assert "name" in item, "Each menu item should contain 'name'"
        assert "url" in item, "Each menu item should contain 'url'"
        assert item["parent"] is None, "Top-level menu items should have 'parent' as None"
        assert item["status"] == "active", "Menu item status should be 'active'"
        for child in item.get("children"):
            assert "id" in child, "Each child menu item should contain 'id'"
            assert "name" in child, "Each child menu item should contain 'name'"
            assert "url" in child, "Each child menu item should contain 'url'"
            assert child["parent"] == item["id"], "Child menu item's 'parent' should match its parent's 'id'"
            assert child["status"] == "active", "Child menu item status should be 'active'"