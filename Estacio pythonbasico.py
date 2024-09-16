import pandas as pd


class InventorySystem:
    def __init__(self):
        # Cria um DataFrame vazio para armazenar o estoque
        self.inventory = pd.DataFrame(columns=['Item', 'Quantity'])

    def add_item(self, item, quantity):
        # Adiciona um item ao estoque ou atualiza a quantidade se o item já existir
        if item in self.inventory['Item'].values:
            self.inventory.loc[self.inventory['Item'] == item, 'Quantity'] += quantity
        else:
            new_item = pd.DataFrame({'Item': [item], 'Quantity': [quantity]})
            self.inventory = pd.concat([self.inventory, new_item], ignore_index=True)
        print(f"Added {quantity} of {item}.")

    def remove_item(self, item, quantity):
        # Remove uma quantidade de um item do estoque
        if item in self.inventory['Item'].values:
            current_quantity = self.inventory.loc[self.inventory['Item'] == item, 'Quantity'].values[0]
            if quantity <= current_quantity:
                self.inventory.loc[self.inventory['Item'] == item, 'Quantity'] -= quantity
                if self.inventory.loc[self.inventory['Item'] == item, 'Quantity'].values[0] == 0:
                    self.inventory = self.inventory[self.inventory['Item'] != item]
                print(f"Removed {quantity} of {item}.")
            else:
                print(f"Error: Not enough {item} in inventory.")
        else:
            print(f"Error: {item} not found in inventory.")

    def view_inventory(self):
        # Exibe o estoque atual
        print("\nCurrent Inventory:")
        print(self.inventory)


# Exemplo de uso do sistema
def main():
    system = InventorySystem()

    # Adicionando itens
    system.add_item('Laranja', 50)
    system.add_item('Goiaba', 30)

    # Removendo itens
    system.remove_item('Laranja', 20)

    # Visualizando o estoque
    system.view_inventory()


if __name__ == "__main__":
    main()
