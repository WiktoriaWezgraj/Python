'''In an operating system, each user has some permissions. The user wants to perform some action that requires specific permissions. 
Write a program that checks whether the user has the required persmission.'''

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = user_permissions.issubset(required_permissions)   # subset
print(has_permissions)  # Will return False because "execute" is missing.