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


# Criteria	Mocking	Stubbing
# Purpose	Simulate the behavior of real objects	Provide fixed, predetermined responses
# Interaction Verification	Can verify method calls and arguments	Typically does not verify interactions
# Complexity	More complex; can simulate various behaviors	Simpler; focuses on providing controlled inputs
# Use Case	Isolate and test code with complex dependencies	Simplify tests by providing known responses
# Recording Behavior	Records how methods were called	Does not record interactions
# State Management	Can maintain state across calls	Usually stateless; returns fixed output
# Framework Support	Primarily uses unittest.mock with features like Mock and MagicMock	Uses unittest.mock's patch for simple replacements
# Flexibility	Highly flexible; can simulate exceptions and side effects	Limited flexibility; focused on return values