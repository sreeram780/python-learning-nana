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


from unittest.mock import patch
# Define the function to be stubbed
def get_user_from_db(user_id):
   # Simulate a complex database operation
   pass
# Test the function with a stub
with patch('__main__.get_user_from_db', return_value={"name": "Prasad", "age": 25}):
   user = get_user_from_db("prasad_id")
   print(user)