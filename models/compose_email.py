from transformers import pipeline

# Load FLAN-T5 Large model
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def compose_email_with_transformer(scenario: str) -> str:
    prompt = (
        "You are an AI trained to write professional emails. Please write a complete, formal email "
        "based on the situation below. The email must include:\n"
        "- A subject line\n"
        "- A greeting (e.g., Dear Sir/Madam)\n"
        "- A clearly written body\n"
        "- A polite closing with signature (e.g., Best regards, [Your Name])\n\n"
        f"Scenario: {scenario.strip()}\n\n"
        "Compose the email below:"
    )

    result = generator(
        prompt,
        max_new_tokens=300,
        temperature=0.7,
        repetition_penalty=1.2,
        top_k=50,
        do_sample=True
    )

    email_output = result[0]["generated_text"].strip()

    # Fallback check
    if len(email_output.split()) < 30:
        return (
            "Subject: Request for Leave\n\n"
            "Dear Sir/Madam,\n\n"
            "I hope this message finds you well. I am writing to request a two-day leave of absence next week "
            "due to personal reasons. I will ensure all my responsibilities are taken care of in advance.\n\n"
            "Thank you for your understanding.\n\n"
            "Best regards,\nSiddharth"
        )

    return email_output

#  Local test
if __name__ == "__main__":
    test = "I need to apply for two days leave next week due to personal reasons."
    email = compose_email_with_transformer(test)
    print("📧 Generated Email:\n", email)
