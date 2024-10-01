# Coffee Machine ☕

This is a simple coffee machine simulator written in Python. The coffee machine allows users to select different types of coffee, manage resources (water, milk, and coffee), process coins, and check available resources.

## Features
- Offers three coffee types:
  - **Espresso**: Made with coffee and water.
  - **Latte**: Made with coffee, milk, and water.
  - **Cappuccino**: Made with coffee, milk, and water.
- Allows users to:
  - View remaining resources using the `report` command.
  - Insert coins to pay for coffee.
  - Refund if insufficient money is provided.
  - Check resource availability before making a coffee.
  - Power off the machine with the `off` command.
  
## How it Works

1. The coffee machine will prompt you to choose a drink: `espresso`, `latte`, or `cappuccino`.
2. You will be prompted to insert coins (quarters, dimes, nickels, and pennies) to pay for the drink.
3. If enough coins are provided, the machine will deduct the necessary resources (water, milk, and coffee) and give back any change.
4. If there are not enough resources or insufficient funds, the machine will notify you.
5. You can also view the remaining resources in the machine by typing `report`.

## Usage

### Prerequisites

You need to have Python installed on your system. The program uses the following modules:

- `replit` for clearing the screen (optional; you can remove this if running locally).
- `time` for adding delays and waiting.
  
### Running the Program

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/coffee-machine.git
    ```

2. Navigate into the project directory:

    ```bash
    cd coffee-machine
    ```

3. Run the program:

    ```bash
    python coffee_machine.py
    ```

4. Follow the on-screen instructions to select drinks, insert coins, and enjoy your virtual coffee!

### Commands

- `report`: Shows the current resource levels (water, milk, coffee, and money).
- `off`: Powers off the machine and exits the program.
- `espresso`, `latte`, `cappuccino`: Selects the corresponding drink.

## Files

- **`coffee_machine.py`**: The main file where the coffee machine logic is implemented.
- **`menu.py`**: Contains the menu and resources data for the different types of coffee.


## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.



