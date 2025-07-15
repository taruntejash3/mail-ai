from transformers import pipeline

# Load upgraded FLAN-T5 model
generator = pipeline("text2text-generation", model="google/flan-t5-large")
def reply_email_with_transformer(received_email: str) -> str:
    """
    Generate a professional reply to a received email using the FLAN-T5 model.
    Parameters:
    - received_email (str): The input email message to reply to.
    Returns:
    - str: A formal reply email.
    """
    prompt = (
        "Reply formally to the following email. Structure the response with a greeting, body, and closing signature.\n\n"
        f"{received_email.strip()}"
    )
    result = generator(
        prompt,
        max_new_tokens=180,
        temperature=0.7,
        top_k=50,
        repetition_penalty=1.3,
        do_sample=True
    )
    return result[0]["generated_text"].strip()

#  Local test
if __name__ == "__main__":
    incoming = "Hi Siddharth, please let us know if you’ll be able to join the IBM presentation tomorrow by 10:30 AM. Kindly confirm your availability."
    response = reply_email_with_transformer(incoming)
    print("\n📩 AI-Generated Reply:\n")
    print(response)
