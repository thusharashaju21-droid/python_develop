
# pip install google-genai mysql-connector-python

import os
from google import genai
from mysql import connector

# MySQL connection
connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="customer_support_db"
)

cursor = connection.cursor()

# Get ticket
query = "SELECT * FROM support_ticket WHERE id = 21;"
cursor.execute(query)

ticket = cursor.fetchone()

print(ticket)

# Check ticket exists
if ticket is None:
    print("Ticket not found")
    exit()

# Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("GEMINI_API_KEY is not set")
    exit()

client = genai.Client(api_key=GEMINI_API_KEY)

# Prompt
prompt = f"""
You are a customer support ticket analysis system.

Analyze the following support ticket.

Customer Name:
{ticket[1]}

Subject:
{ticket[3]}

Description:
{ticket[4]}

Provide the following information:

1. Category
2. Priority
3. Sentiment
4. Summary
5. Suggested response

Category must be one of:

payment
delivery
account
technical
refund
other

Priority must be one of:

low
medium
high
urgent

Sentiment must be one of:

positive
neutral
negative

Return the answer in a clear format.
"""

# Gemini response
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print(response.text)

# Close database connection
cursor.close()
connection.close()

 
