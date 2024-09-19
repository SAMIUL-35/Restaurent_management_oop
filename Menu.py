class menu:
    def __init__(self):
        self.items = []

    def add_menu(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('Item deleted successfully')
        else:
            print('Item not found')

    def show_menu_item(self):
        for item in self.items:
            print(f'Item name: {item.name}')
            print(f'Item price: {item.price}')
            print(f'Item quantity: {item.quantity}')
            print('--------------------')