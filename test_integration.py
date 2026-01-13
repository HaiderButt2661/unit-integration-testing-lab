# test_integration.py
import pytest
from bank_app import transfer, calculate_interest

# Example Integration Tests for the transfer function
def test_integration_transfer_successful():
    """Test a successful transfer updates both balances correctly."""
    balance1 = 1000
    balance2 = 500
    amount = 200
    new_balance1, new_balance2 = transfer(balance1, balance2, amount)
    assert new_balance1 == 800
    assert new_balance2 == 700

def test_integration_transfer_insufficient_balance_failure():
    """Test transfer failure due to insufficient balance in the source account."""
    balance1 = 50
    balance2 = 500
    amount = 100
    with pytest.raises(ValueError, match="Insufficient balance"):
        # The withdraw function called inside transfer will raise this exception
        transfer(balance1, balance2, amount)
    # Verify balances remain unchanged if transaction fails
    assert balance1 == 50
    assert balance2 == 500

# Example of a combined workflow test
def test_integration_transfer_then_interest_calculation():
    """Test a combined workflow: successful transfer followed by interest calculation."""
    balance_from = 2000
    balance_to = 1000
    transfer_amount = 500
    rate = 5
    years = 1

    # Perform the transfer (Integration part 1)
    updated_balance_from, updated_balance_to = transfer(balance_from, balance_to, transfer_amount)
    assert updated_balance_from == 1500
    assert updated_balance_to == 1500

    # Calculate interest on the new balances (Integration part 2)
    interest_from = calculate_interest(updated_balance_from, rate, years)
    interest_to = calculate_interest(updated_balance_to, rate, years)

    # Verify the results
    assert abs(interest_from - 1575.00) < 0.001
    assert abs(interest_to - 1575.00) < 0.001
