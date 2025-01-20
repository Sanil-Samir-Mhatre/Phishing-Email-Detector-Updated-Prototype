# Phishing-Email-Detector-Updated-Prototype
A Flask-based application to detect phishing emails using machine learning and rule-based checks, with email flagging and dashboard functionalities.
(This one inputs multiple emails in text fromat and then detects the Phising traits in them.)

# Phishing Email Detection Application

## Overview
This is a Flask-powered web application designed to detect phishing emails in bulk. The system leverages a machine learning model combined with rule-based heuristics to classify emails as phishing or legitimate. A dashboard is also available to review flagged emails and understand suspicious traits.

---

## Features
- **Multi-email detection**: Paste multiple emails together for a single bulk detection process.
- **Machine learning model**: Classifies emails as phishing or legitimate based on their content.
- **Rule-based checks**: Looks for traits often associated with phishing, such as suspicious links or sensitive information requests.
- **Flagging system**: Emails flagged with phishing traits are stored and displayed in a dashboard.
- **User-friendly interface**: Web-based UI for email submission and results review.

---

## How It Works
1. **Train the Model**: The ML model is trained (by the function `train_model`) and deployed with the application.
2. **Email Submission**: Users submit multiple email texts, separated by a delimiter (`---` or double line breaks).
3. **Email Validation**: Check each segment for email-like characteristics (optional validation).
4. **Detection**:
   - **ML Classification**: Predict whether an email is phishing or legitimate.
   - **Rule-based Heuristics**: Analyze content for phishing traits, such as keywords, suspicious links, capitalization, etc.
5. **Flagging**: Emails predicted as phishing or with detected traits are flagged and entered into the dashboard.
6. **Dashboard**: Displays flagged emails with accompanying phishing traits.

---

## Installation

### Requirements
- Python 3.8+
- Flask
- Required libraries in `requirements.txt` (if available).

### Steps
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Access the application at `http://127.0.0.1:5000`.

---

## Usage
### Submitting Emails
1. Go to the homepage.
2. Paste multiple emails in the input box, separated by `---` or two newlines for distinction.
3. Click the submit button to process the emails.

### Reviewing Results
- Results for each email (phishing/legitimate and traits) will display on the results page.
- Flagged emails will be stored in the dashboard for further analysis.

---

## Technical Details

### Machine Learning Model
The model is trained beforehand using the `train_model` function, which generates both a classifier and a vectorizer.

### Rule-based Detection
- **Keywords**: Identifies phishing-related terminology.
- **Suspicious Links**: Detects links with patterns resembling possible phishing attempts.
- **Requests for Personal Info**: Scans for sensitive information requests, e.g., "password", "credit card", etc.
- **Language Issues**: Flags excessive capitalization and other simplistic language patterns.

---

## Future Enhancements
- Support for file uploads (e.g., `.txt` files).
- Adding advanced NLP techniques for enhanced detection.
- Providing download options for flagged emails and reports.
- Integration with external email systems.

---

## License
This project is licensed under [MIT License](LICENSE).

---

## Acknowledgments
- Flask Framework: For enabling rapid development of web applications.
- Scikit-learn: For model training and vectorization.
- Regex: Used for enabling flexible and rule-based detection.
