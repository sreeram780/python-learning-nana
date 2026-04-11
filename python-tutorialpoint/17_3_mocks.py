from unittest.mock import Mock
# Create a mock object
database = Mock()
# Simulate a method call
database.get_user.return_value = {"name": "Prasad", "age": 30}
# Use the mock object
user = database.get_user("prasad_id")
print(user)  
# Verify the interaction
database.get_user.assert_called_with("prasad_id")