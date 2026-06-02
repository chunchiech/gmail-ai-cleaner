from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def classify_email(subject):

    response = client.responses.create(
        model="gpt-5",
        input=f"""
Classify this email subject.

Subject:
{subject}

Return only one word:

important
newsletter
advertisement
spam
"""
    )

    return response.output_text.strip()


if __name__ == "__main__":
    subject = "🔥 Limited Time Sale 90% OFF"

    result = classify_email(subject)

    print(result)
