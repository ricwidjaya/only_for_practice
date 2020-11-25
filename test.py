# Password Validation
# 1. At least 8 characters
# 2. Contain any sort of letters, numbers and !@#$%^&*

import re

pattern = re.compile(r'^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')

while True:
