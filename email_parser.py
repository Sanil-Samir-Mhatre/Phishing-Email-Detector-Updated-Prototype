def parse_email(stream):
    from email import message_from_binary_file
    from email.policy import default

    # Parse the email from the uploaded file stream
    msg = message_from_binary_file(stream, policy=default)

    # Extract key metadata and plain text content
    email_data = {
        "From": msg["From"],
        "To": msg["To"],
        "Subject": msg["Subject"],
        "Date": msg["Date"],
        "Content": msg.get_body(preferencelist=("plain")).get_content() if msg.is_multipart() else msg.get_payload()
    }

    return email_data
