"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement
        #Arrange
        calc = Calculator()
        a = 9
        b = 4
        expected = 5

        #Act
        result = calc.subtract(a,b)

        #Assert
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""

        #Arrange
        calc = Calculator()
        a = -5 
        b = -3
        expected = -2

        #Act
        result = calc.subtract(a,b)

        #Assert 
        assert result == expected

    def test_subtract_positive_and_negative(self):
        """Test subtracting positive and negative numbers."""

        #Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 8

        #Act
        result = calc.subtract(a,b)

        #Assert
        assert result == expected

    def test_subtract_negative_and_positive(self):
        """Test subtracting negative and positive numbers."""

        #Arrange
        calc = Calculator()
        a = -9
        b = 3
        expected = -12

        #Act
        result = calc.subtract(a,b)

        #Assert
        assert result == expected


    def test_subtract_positive_with_zero(self):
        """Test subtracting positive number with zero."""

        #Arrange
        calc = Calculator()
        a = 9
        b = 0
        expected = 9

        #Act
        result = calc.subtract(a,b)

        #Assert
        assert result == expected

    def test_subtract_zero_with_positive(self):
        """Test subtracting zero with positive number."""

        #Arrange
        calc = Calculator()
        a = 0
        b = 3
        expected = -3

        #Act
        result = calc.subtract(a,b)

        #Assert
        assert result == expected

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""

        #Arrange
        calc = Calculator()
        a = 5.9
        b = 2.2
        expected = 3.7

        #Act
        result = calc.subtract(a,b)

        #Assert
        assert result == pytest.approx(expected)

    # def test_subtract_invalid_input(self):
    #     """Test subtracting with invalid input."""
    #     # Arrange
    #     calc = Calculator()
    #     a = "five"
    #     b = 3

    #     # Act & Assert
    #     with pytest.raises(InvalidInputException):
    #         calc.subtract(a, b)

    def test_subtract_large_numbers(self):
        """Test subtracting large numbers."""
        # Arrange
        calc = Calculator()
        a = 10000
        b = 9999 
        expected = 1    

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_boundary_values(self):
        """Test subtracting boundary values."""
        # Arrange
        calc = Calculator()
        a = Calculator.MAX_VALUE
        b = Calculator.MIN_VALUE
        expected = Calculator.MAX_VALUE - Calculator.MIN_VALUE

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # TODO: Implement
        #Arrange
        calc = Calculator()
        a = 3
        b = 5
        expected = 15
        
        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == expected
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        #Arrange
        calc = Calculator()
        a = -4
        b = -2
        expected = 8

        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == expected
    
    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative numbers."""
        #Arrange
        calc = Calculator()
        a = 6
        b = -3
        expected = -18

        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == expected
    
    def test_multiply_negative_and_positive(self):
        """Test multiplying negative and positive numbers."""
        #Arrange
        calc = Calculator()
        a = -7
        b = 4
        expected = -28

        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == expected

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        #Arrange
        calc = Calculator()
        a = 9
        b = 0
        expected = 0

        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == expected

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        #Arrange
        calc = Calculator()
        a = 2.5
        b = 4.0
        expected = 10.0

        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == pytest.approx(expected)
    
    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        #Arrange
        calc = Calculator()
        a = 10000
        b = 20009
        expected = 200090000

        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == expected

    def test_multiply_large_number_by_zero(self):
        """Test multiplying a large number by zero."""

        #Arrange
        calc = Calculator()
        a = 103045
        b = 0
        expected = 0

        #Act
        result = calc.multiply(a,b)

        #Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # TODO: Implement
        #Arrange
        calc = Calculator()
        a = 8
        b = 2
        expected = 4

        #Act
        result = calc.divide(a,b)

        #Assert
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        #Arrange
        calc = Calculator()
        a = -9
        b = -3
        expected = 3

        #Act
        result = calc.divide(a,b)

        #Assert
        assert result == expected
    
    def test_divide_positive_and_negative(self):
        """Test dividing positive and negative numbers."""
        #Arrange
        calc = Calculator()
        a = 10
        b = -2
        expected = -5

        #Act
        result = calc.divide(a,b)

        #Assert
        assert result == expected
    
    def test_divide_negative_and_positive(self):
        """Test dividing negative and positive numbers."""
        #Arrange
        calc = Calculator()
        a = -15
        b = 3
        expected = -5

        #Act
        result = calc.divide(a,b)

        #Assert
        assert result == expected
    
        
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        #Arrange
        calc = Calculator()
        a = 7.5
        b = 2.5
        expected = 3.0

        #Act
        result = calc.divide(a,b)

        #Assert
        assert result == pytest.approx(expected)

    def test_divide_zero_by_large_number(self):
        """Test dividing zero by a large number."""
        #Arrange
        calc = Calculator()
        a = 0
        b = 1_000_000
        expected = 0

        #Act
        result = calc.divide(a,b)

        #Assert
        assert result == expected
    
    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError with correct message."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

class TestPower:
    """Tests for the power method."""

    def test_power_positive_exponent(self):
        """Test raising to a positive exponent."""

        #Arrange
        calc = Calculator()
        a = 2
        b = 3
        expected = 8

        #Act
        result = calc.power(a,b)

        #Assert
        assert result == expected

    def test_power_negative_exponent(self):
        """Test raising to a negative exponent."""

        #Arrange
        calc = Calculator()
        a = 2
        b = -2
        expected = 0.25

        #Act
        result = calc.power(a,b)

        #Assert
        assert result == pytest.approx(expected)

    def test_power_zero_exponent(self):
        """Test raising to the zero exponent."""

        #Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 1

        #Act
        result = calc.power(a,b)

        #Assert
        assert result == expected

    def test_power_fractional_exponent(self):
        """Test raising to a fractional exponent."""

        #Arrange
        calc = Calculator()
        a = 9
        b = 0.5
        expected = 3

        #Act
        result = calc.power(a,b)

        #Assert
        assert result == pytest.approx(expected)
    
    def test_power_zero_base(self):
        """Test zero base with positive exponent."""

        #Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 0

        #Act
        result = calc.power(a,b)

        #Assert
        assert result == expected

class TestSquareRoot:
    '''Tests for the square_root method.'''

    def test_square_root_positive_number(self):
        """Test square root of a positive number."""

        #Arrange
        calc = Calculator()
        a = 16
        expected = 4

        #Act
        result = calc.square_root(a)

        #Assert
        assert result == expected
    
    def test_square_root_zero(self):
        """Test square root of zero."""

        #Arrange
        calc = Calculator()
        a = 0
        expected = 0

        #Act
        result = calc.square_root(a)

        #Assert
        assert result == expected

    def test_square_root_non_perfect_square(self):
        """Test square root of a non-perfect square."""

        #Arrange
        calc = Calculator()
        a = 20
        expected = 4.47213595499958

        #Act
        result = calc.square_root(a)

        #Assert
        assert result == pytest.approx(expected)

class TestModulo:
    '''Tests for the modulo method.'''

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""

        #Arrange
        calc = Calculator()
        a = 10
        b = 3
        expected = 1

        #Act
        result = calc.modulo(a,b)

        #Assert
        assert result == expected
    
    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""

        #Arrange
        calc = Calculator()
        a = -10
        b = -3
        expected = -1

        #Act
        result = calc.modulo(a,b)

        #Assert
        assert result == expected

    def test_modulo_positive_and_negative(self):
        """Test modulo with positive and negative numbers."""

        #Arrange
        calc = Calculator()
        a = 10
        b = -3
        expected = -2

        #Act
        result = calc.modulo(a,b)

        #Assert
        assert result == expected

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError with correct message."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            calc.modulo(10, 0)


class TestValidationAndBoundaries:
    """Advanced tests for boundaries and exceptions."""
    
    def test_boundaries(self):
        calc = Calculator()
        # within boundaries (should not raise error)
        assert calc.add(1000000, -1000000) == 0
        
        # out-of-boundary
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 0)
        with pytest.raises(InvalidInputException):
            calc.add(0, -1000001)

    def test_subtract_out_of_bounds(self):
        """Test subtracting with out-of-bounds input to kill validation mutant."""
        calc = Calculator()
        # Input a number that exceeds the limit
        with pytest.raises(InvalidInputException):
            calc.subtract(1000001, 1)


    def test_argument_positions(self):
        calc = Calculator()
        
        with pytest.raises(InvalidInputException):
            calc.multiply(1, 1000001)
        with pytest.raises(InvalidInputException):
            calc.divide(1, 1000001)
            
    def test_error_messages(self):
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(1, 0)
    
    def test_power_validation(self):
        """Test validation for power method."""
        calc = Calculator()
        with pytest.raises(InvalidInputException, match="out of range"):
            calc.power(1000001, 2)
        with pytest.raises(InvalidInputException, match="out of range"):
            calc.power(2, 1000001)

    def test_square_root_validation(self):
        """Test validation for square_root method."""
        calc = Calculator()
        with pytest.raises(InvalidInputException, match="out of range"):
            calc.square_root(1000001)

    def test_modulo_validation(self):
        """Test validation for modulo method."""
        calc = Calculator()
        with pytest.raises(InvalidInputException, match="out of range"):
            calc.modulo(1000001, 5)
        with pytest.raises(InvalidInputException, match="out of range"):
            calc.modulo(5, 1000001)
            
    def test_error_messages(self):
        """Test specific value error messages."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(1, 0)
        with pytest.raises(ValueError, match="Cannot modulo by zero"):
            calc.modulo(10, 0)
        with pytest.raises(ValueError, match="negative number"):
            calc.square_root(-1)