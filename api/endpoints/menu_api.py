class MenuAPI:
    MENU_ENDPOINT = "/api/v1/menu/menu-partner-shop/get-menu-roles"
    def __init__(self, client):
        self.client = client

    def get_menu(self):
        return self.client.get(self.MENU_ENDPOINT)