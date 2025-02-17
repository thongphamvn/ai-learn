import os

from dotenv import load_dotenv
from httpx import get
from openai import OpenAI

load_dotenv()
openai_key = os.getenv("OPENAI_KEY")


# init OpenAI
openai = OpenAI(api_key=openai_key)


def get_completion(msgs):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msgs,
        temperature=0.0,
        max_tokens=500,
    )
    return response.choices[0].message.content


delimiter = "####"

system_message = f"""You will be provided with customer service queries. \
The customer service query will be delimited with \
{delimiter} characters.
Classify each query into a primary category \
and a secondary category. 
Provide your output in json format with the \
keys: primary and secondary.

Primary categories: Billing, Technical Support, \
Account Management, or General Inquiry.

Billing secondary categories:
Unsubscribe or upgrade
Add a payment method
Explanation for charge
Dispute a charge

Technical Support secondary categories:
General troubleshooting
Device compatibility
Software updates

Account Management secondary categories:
Password reset
Update personal information
Close account
Account security

General Inquiry secondary categories:
Product information
Pricing
Feedback
Speak to a human
"""

# user_message = f'''I want you to delete my profile and all of my user data"""'''

# msgs = [
#     {"role": "system", "content": system_message},
#     {"role": "user", "content": user_message},
# ]

# response = get_completion(msgs)
# print(response)


user_message = f"""\
hi hello"""
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": f"{delimiter}{user_message}{delimiter}"},
]
response = get_completion(messages)
print(response)
