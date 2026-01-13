# test_unit.py
import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility

# Example Unit Tests for deposit function
def test_deposit_valid_amount():
    assert deposit(100, 50) == 150

def test_deposit_boundary_amount():
    assert deposit(100, 0.01) == 100.01

def test_deposit_invalid_amount_zero():
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        deposit(100, 0)

def test_deposit_invalid_amount_negative():
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        deposit(100, -50)

# Example Unit Tests for withdraw function
def test_withdraw_valid_amount():
    assert withdraw(100, 50) == 50

def test_withdraw_invalid_amount_zero():
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        withdraw(100, 0)

def test_withdraw_invalid_insufficient_balance():
    with pytest.raises(ValueError, match="Insufficient balance"):
        withdraw(50, 100)


def test_calculate_interest_valid_inputs():   
    assert abs(calculate_interest(1000, 5, 2) - 1102.50) < 0.001

def test_calculate_interest_invalid_balance_negative():
    with pytest.raises(ValueError, match="Balance cannot be negative"):
        calculate_interest(-1000, 5, 2)

def test_check_loan_eligibility_eligible():
    """Test case where user is eligible."""
    assert check_loan_eligibility(5000, 700) is True 
def test_check_loan_eligibility_not_eligible_balance():
    """Test case where balance is too low."""
    assert check_loan_eligibility(4999, 700) is False

def test_check_loan_eligibility_not_eligible_credit():
    """Test case where credit score is too low."""
    assert check_loan_eligibility(5000, 699) is False

def test_check_loan_eligibility_invalid_balance_negative():
    """Test loan eligibility check with negative balance should raise ValueError."""
    with pytest.raises(ValueError, match="Balance cannot be negative"):
        check_loan_eligibility(-100, 700)
