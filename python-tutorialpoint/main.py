Public vs Protected vs Private Variables
Here is a tabular comparison of Public, Protected, and Private variables in Python −

Feature	Public Variables	Protected Variables	Private Variables
Definition	Variables that can be accessed from anywhere.	Variables that can be accessed within the class and its subclasses.	Variables that can only be accessed within the class they are defined in.
Syntax	int var	int _var	int __var
Security	Least secure	Moderately secure	Most secure
Example	int age = 25	int _age = 25	int __age = 25