import re

# This finds email addresses
def find_emails(text):
    email_pattern = r'\w+@\w+\.\w+'
    emails = re.findall(email_pattern, text)
    return emails

# This finds website links
def find_links(text):
    link_pattern = r'https?://\S+'
    links = re.findall(link_pattern, text)
    return links

# This finds phone numbers
def find_phones(text):
    phone_pattern = r'\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}'
    phones = re.findall(phone_pattern, text)
    return phones

# This finds hashtags 
def find_hashtags(text):
    hashtag_pattern = r'#\w+'
    hashtags = re.findall(hashtag_pattern, text)
    return hashtags

# This finds money amounts 
def find_money(text):
    money_pattern = r'\$\d+\.\d{2}'
    money = re.findall(money_pattern, text)
    return money

# This tests all the functions
def test_functions():
    test_text = """
    Contact me at test@school.com or help@website.org.
    Our site is https://myschool.edu and http://learn.org.
    Call 555-123-4567 or (987) 654-3210.
    Follow #coding and #python for tips.
    The price is $19.99 and $25.00.
    """
    
    print("Found emails:", find_emails(test_text))
    print("Found links:", find_links(test_text))
    print("Found phones:", find_phones(test_text))
    print("Found hashtags:", find_hashtags(test_text))
    print("Found money:", find_money(test_text))

# Run the test
test_functions()
