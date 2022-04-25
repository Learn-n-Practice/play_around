import random


class Customer:
    """ This is a class that manages customers"""
    account_types = {'S': 'Savings', 'C': 'Current', 'YS': 'Youth Savings'}
    act_no_prefix = {'S': 1441, 'C': 1442, 'YS': 1443}

    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.account_type = str()
        self.account_number = None
        self.balance = float()

    # Setters
    def set_name(self, name):
        """Sets customer's name. Takes name as an input"""
        self.name = name

    def set_age(self, age):
        """Sets customer's age. Takes age as an input"""
        self.age = age

    # Getters
    def get_name(self):
        """Returns customer's name. Takes no input"""
        return self.name

    def get_age(self):
        """Returns customer's age. Takes no input"""
        return self.age

    def get_balance(self):
        """Returns customer's account balance"""
        if self.account_number:
            return {'balance': self.balance}
        else:
            return {'balance': 'You have no account records'}

    def get_account_details(self):
        """Returns customer's account type and account number"""
        return {
            'name': self.name,
            'account_type': self.account_type,
            'account_number': self.account_number,
            'balance': self.balance,
        }

    def create_account(self):
        """Creates an account for the customer."""
        print(self.account_types)
        act_type = input("Enter the appropriate abbreviation for your Account Type: ").strip().upper()
        self.account_type = self.account_types[act_type]
        acctno = str(self.act_no_prefix[act_type])
        for i in range(10):
            acctno += str(random.randint(0,9))
        self.account_number = acctno
        return {
            'message': 'Account created successfully',
            'account': self.account_number
        }

    def deposit(self, amount):
        """Credits a customer's account with amount. Takes amount as input."""
        if self.account_number:
            self.balance += amount
            return {
                'message': f'Deposited Gh¢{float(amount)}',
                'account': self.account_number,
                'balance': self.balance,
            }
        else:
            print("Create Account to Deposit")
            self.create_account()
            return self.deposit(amount)

    def withdraw(self, amount):
        """Debits a customer's account with amount. Takes amount as input"""
        if self.account_number:
            if self.balance >= amount:
                self.balance -= amount
                return {
                    'message': f'Withdrawn {amount}.00',
                    'account': self.account_number,
                    'balance': self.balance
                }
            else:
                return {'message':f"You can only withdraw a maximum of Gh¢{self.balance}"}
        else:
            print("You do not have an account")
            create = input("Create a new account? (Y/N): ").strip().lower()
            if create == 'y':
                return self.create_account()
            else:
                return {'message': 'We are here to assist whenever you are ready to create your account'}


