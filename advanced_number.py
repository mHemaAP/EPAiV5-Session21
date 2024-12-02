class AdvancedNumber:
    """
    A class that encapsulates a numeric value and supports arithmetic, 
    comparison operations, and other Python special methods.
    """
    def __init__(self, value=0):
        """
        Initializes the AdvancedNumber with a given value.

        Args:
            value (int, float): The numeric value to be encapsulated. Defaults to 0.
        """
        self.value = value

    def __str__(self):
        """
        Returns a user-friendly string representation of the object.

        Returns:
            str: A formatted string showing the value of the object.
        """
        return f"Value: {self.value}"

    def __repr__(self):
        """
        Returns a detailed string representation for debugging.

        Returns:
            str: A string in the format 'AdvancedNumber(value)'.
        """
        return f"AdvancedNumber({self.value})"

    def __add__(self, other):
        """
        Adds two AdvancedNumber objects.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            AdvancedNumber: A new object with the sum of the two values.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if not isinstance(other, AdvancedNumber):
            raise ValueError("Operand must be of type AdvancedNumber")
        return AdvancedNumber(self.value + other.value)

    def __sub__(self, other):
        """
        Subtracts another AdvancedNumber object from the current one.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            AdvancedNumber: A new object with the difference of the two values.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if not isinstance(other, AdvancedNumber):
            raise ValueError("Operand must be of type AdvancedNumber")
        return AdvancedNumber(self.value - other.value)
    
    def __mul__(self, other):
        """
        Multiplies the current object with another number.

        Args:
            other (AdvancedNumber, int, float): The object or number to multiply.

        Returns:
            AdvancedNumber: A new object with the product of the multiplication.

        Raises:
            ValueError: If the operand is not AdvancedNumber, int, or float.
        """
        if isinstance(other, (AdvancedNumber, int, float)):
            return AdvancedNumber(self.value * (other.value if isinstance(other, AdvancedNumber) else other))
        raise ValueError("Operand must be AdvancedNumber, int, or float")

    def __truediv__(self, other):
        """
        Divides the current object by another number.

        Args:
            other (AdvancedNumber, int, float): The object or number to divide by.

        Returns:
            AdvancedNumber: A new object with the quotient.

        Raises:
            ValueError: If the operand is not AdvancedNumber, int, or float.
            ValueError: If attempting to divide by zero.
        """
        if isinstance(other, (AdvancedNumber, int, float)):
            divisor = other.value if isinstance(other, AdvancedNumber) else other
            if divisor == 0:
                raise ValueError("Cannot divide by zero")
            return AdvancedNumber(self.value / divisor)
        raise ValueError("Operand must be AdvancedNumber, int, or float")

    def __mod__(self, other):
        """
        Computes the modulus with another AdvancedNumber.

        Args:
            other (AdvancedNumber, int, float): Another AdvancedNumber object, int, or float.

        Returns:
            AdvancedNumber: A new object with the modulus result.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber, int, or float.
        """
        if isinstance(other, (AdvancedNumber, int, float)):
            return AdvancedNumber(self.value % (other.value if isinstance(other, AdvancedNumber) else other))
        raise ValueError("Operand must be AdvancedNumber, int, or float")

    def __lt__(self, other):
        """
        Checks if the current value is less than another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if lesser, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value < other.value
        raise ValueError("Operand must be of type AdvancedNumber")

    def __le__(self, other):
        """
        Checks if the current value is less than or equal to another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if lesser or equal, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value <= other.value
        raise ValueError("Operand must be of type AdvancedNumber")

    def __gt__(self, other):
        """
        Checks if the current value is greater than another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if greater, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value > other.value
        raise ValueError("Operand must be of type AdvancedNumber")

    def __ge__(self, other):
        """
        Checks if the current value is greater than or equal to another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if greater or equal, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value >= other.value
        raise ValueError("Operand must be of type AdvancedNumber")

    def __eq__(self, other):
        """
        Checks if the current value is equal to another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if equal, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if other is self:  # Only equal if it's the exact same object
            return True
        if isinstance(other, AdvancedNumber):
            return False  # Different objects are never equal
        return self.value == other

    def __ne__(self, other):
        """
        Checks if the current value is not equal to another.

        Args:
            other (AdvancedNumber): Another AdvancedNumber object.

        Returns:
            bool: True if not equal, False otherwise.

        Raises:
            ValueError: If other is not an instance of AdvancedNumber.
        """
        if isinstance(other, AdvancedNumber):
            return self.value != other.value
        raise ValueError("Operand must be of type AdvancedNumber")

    def __hash__(self):
        """
        Returns the hash value of the object.

        Returns:
            int: The hash of the value.
        """
        return hash(self.value)

    def __bool__(self):
        """
        Returns the boolean value of the object.

        Returns:
            bool: True if the value is non-zero, False otherwise.
        """
        return bool(self.value)

    def __call__(self):
        """
        Makes the object callable, returning the square of its value.

        Returns:
            int, float: The square of the current value.
        """
        return self.value ** 2

    def __format__(self, format_spec):
        if format_spec == '#x' and isinstance(self.value, int):
            return hex(self.value)
        return format(self.value, format_spec)

    def __del__(self):
        """
        Destructor called when the object is about to be destroyed.
        Prints a message indicating the value being destroyed.
        """
        print(f"AdvancedNumber with value {self.value} is being destroyed")