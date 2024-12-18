import spacy

nlp = spacy.load("en_core_web_sm")

def process_user_query(user_input: str) -> str:
    doc = nlp(user_input)
    # Simple response generation
    if "investment" in [token.text for token in doc]:
        return "Let's look at your investment options..."
    return "I'm not sure I understand. Can you rephrase?"
