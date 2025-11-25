program 16
code:
import re
text = "Contact us at support@example.com or sales@company.org for more info."
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)
email_dict = {email: email.split('@')[1] for email in emails}
print(email_dict)
program 17
code:
import re
from collections import Counter
text = "Alice met Bob. Alice and Bob went to Paris. Bob liked Paris."
pattern = r'\b[A-Z][a-zA-Z]*\b'
capital_words = re.findall(pattern, text)
word_count = dict(Counter(capital_words))
print(word_count)
program 18
code:
square_dict = {}
for num in range(1, 6):
    square_dict[num] = num * num
print(square_dict)
program 19
code:
import re
from collections import Counter
text = "I bought 3 apples, 4.5 kg of mangoes, and 3 more oranges. Total: 7.5 kg."
pattern = r'\b\d+(?:\.\d+)?\b'
numbers = re.findall(pattern, text)
number_count = dict(Counter(numbers))
print(number_count)
program 20
code:
import re
log = """ User: alice IP: 192.168.1.10
User: bob IP: 10.0.0.2
User: alice IP: 192.168.1.11
User: bob IP: 10.0.0.2 """
pattern = r'User:\s*(\w+)\s*IP:\s*([\d\.]+)'
matches = re.findall(pattern, log)
user_ips = {}
for username, ip in matches:
    if username not in user_ips:
        user_ips[username] = []
    if ip not in user_ips[username]:  
        user_ips[username].append(ip)
print(user_ips)
