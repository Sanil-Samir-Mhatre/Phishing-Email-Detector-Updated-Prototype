from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd


def train_model():
    """
    Train a Naive Bayes model to detect phishing emails.
    Returns the trained model and the vectorizer.
    """
    # Step 1: Build a dataset
    data = {
        "email_text": [
            "Congratulations, you won a free iPhone!",
            "Update your account to avoid suspension.",
            "Meeting tomorrow at 10 AM in the conference room.",
            "Don't forget to submit your report by EOD.",
            "Suspicious login detected. Click here to secure your account."
        ],
        "label": [1, 1, 0, 0, 1]  # 1 = Phishing, 0 = Legitimate
    }
    df = pd.DataFrame(data)

    # Step 2: Vectorize the text data
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["email_text"])
    y = df["label"]

    # Step 3: Train Multinomial Naive Bayes Model
    model = MultinomialNB()
    model.fit(X, y)

    print("Model training complete.")

    # Step 4: Return the trained model and vectorizer
    return model, vectorizer
