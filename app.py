from flask import Flask, request, render_template
from train_model import train_model
import re

# Initialize Flask application
app = Flask(__name__)

# Train the model and load it along with the vectorizer
model, vectorizer = train_model()

# List to store flagged emails for the dashboard
flagged_emails = []


def detect_phishing_traits(email):
    """
    Rule-based detection for phishing-related traits.
    :param email: Input email content (as a string).
    :return: List of phishing traits found.
    """
    phishing_traits = []

    # Example rules-based checks:
    # 1. Check for common phishing keywords
    keywords = ["urgent", "free", "winner", "claim", "limited offer", "act now"]
    if any(word in email.lower() for word in keywords):
        phishing_traits.append("Email contains suspicious keywords.")

    # 2. Suspicious link checks
    if re.search(r"http[s]?://[\w./-]+", email):
        phishing_traits.append("Email contains suspicious links.")

    # 3. Attempts to collect personal information
    if re.search(r"password|account|credit card|login", email.lower()):
        phishing_traits.append("Email seeks sensitive personal details.")

    # 4. Grammar and spelling mistakes (simplified rule example)
    if len(re.findall(r"[A-Z]{2,}", email)) > 5:  # Mock detection of many uppercase words
        phishing_traits.append("Email contains excessive capitalization.")

    return phishing_traits


@app.route("/")
def index():
    """
    Render the homepage with a form to input multiple email texts.
    """
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def detect():
    """
    Handle form submission to detect phishing emails for multiple emails.
    """
    # Retrieve the input text containing multiple emails
    raw_email_input = request.form.get("email_texts", "").strip()

    # Split emails by a clear delimiter (e.g., "---" or line breaks)
    # Supports users who input emails separated by "---" or "\n\n" (two newlines for separation)
    email_entries = re.split(r"(?:---|\n\s*\n)", raw_email_input)

    results = []  # To store results for all processed emails

    for email_text in email_entries:
        email_text = email_text.strip()  # Remove any leading or trailing whitespace
        if not email_text:
            continue  # Skip empty segments

        # Detect valid emails by checking for context (e.g., subject lines or email-like formatting)
        if not is_valid_email(email_text):
            continue  # Skip non-email-like content

        # Vectorize the input text
        email_vector = vectorizer.transform([email_text])

        # Perform prediction using the trained model
        prediction = model.predict(email_vector)

        # Interpret prediction (machine learning output)
        ml_result = "Phishing Email" if prediction[0] == 1 else "Legitimate Email"

        # Perform rule-based phishing traits detection
        phishing_traits = detect_phishing_traits(email_text)

        # Flag email when phishing is detected
        if ml_result == "Phishing Email" or phishing_traits:
            flagged_emails.append({"email_text": email_text, "traits": phishing_traits})

        # Store the result for each email
        results.append({
            "email_text": email_text,
            "ml_result": ml_result,
            "phishing_traits": phishing_traits
        })

    # Render the result page with all emails and their results
    return render_template("results.html", results=results)


def is_valid_email(email_text):
    """
    Check if the provided text segment looks like an email.
    :param email_text: String segment potentially containing an email.
    :return: Boolean indicating whether it seems like a valid email.
    """
    # Basic heuristic checks to determine if a text looks like an email
    # 1. Check for the presence of typical email headers
    headers = ["subject:", "date:", "from:", "to:"]
    if any(header in email_text.lower() for header in headers):
        return True

    # 2. Check content length - ignore overly short or nonsensical entries
    if len(email_text) < 20:  # Too small to be a valid email
        return False

    # 3. Look for common email keywords
    keywords = ["dear", "sincerely", "regards", "kindly", "unsubscribe"]
    if any(word in email_text.lower() for word in keywords):
        return True

    return False


@app.route("/dashboard")
def dashboard():
    """
    Displays a dashboard of flagged emails with traits and alerts.
    """
    return render_template("dashboard.html", flagged_emails=flagged_emails)


if __name__ == "__main__":
    """
    Run the Flask application.
    """
    app.run(debug=True)
