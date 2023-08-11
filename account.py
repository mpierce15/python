class Account:
    def __init__(self, name: str) -> None:
        """
        Initializes an Account object.

        :param name: The name associated with the account.
        :type name: str
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposits amount into the account if > 0.

        :param amount: The amount to be deposited.
        :type amount: float

        :return: True if the deposit was successful, False otherwise.
        :rtype: bool
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the supplied amount that is >0 and < the account balance.

        :param amount: Amount to be withdrawn.
        :type amount: float

        :return: True if withdrawal was successful, otherwise False.
        :rtype: bool
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Returns the account balance.

        :return: Account balance.
        :rtype: float
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Returns the name of the account.

        :return: Account name.
        :rtype: str
        """
        return self.__account_name
