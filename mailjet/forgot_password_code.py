forgot_password_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your One-Time Login Code</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .email-container {{
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }}
        .email-header {{
            text-align: center;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }}
        .email-body {{
            font-size: 16px;
            color: #333333;
            margin-bottom: 20px;
        }}
        .code-box {{
            font-size: 20px;
            font-weight: bold;
            color: #4CAF50;
            background-color: #f4f4f4;
            padding: 10px;
            border: 2px solid #4CAF50;
            display: inline-block;
            margin: 10px 0;
        }}
        .footer {{
            font-size: 14px;
            color: #777777;
            text-align: center;
            margin-top: 20px;
        }}
        .footer a {{
            color: #4CAF50;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="email-header">
            <h2>Your One-Time Login Code</h2>
        </div>
        <div class="email-body">
            <p>Hello <strong>{full_name}</strong>,</p>
            <p>We received a request to help you log into your account. Use the one-time code below to complete the process.</p>
            <p class="code-box">{one_time_code}</p>
            <p>This code will expire in <strong>{expiration_time}</strong>. If you didn’t request this, please disregard this email. For your security, do not share this code with anyone.</p>
            <p>If you need further assistance, please reach out to our support team.</p>
        </div>
        <div class="footer">
            <p>Thank you,</p>
            <p>Email: <a href="mailto:{support_email}">{support_email}</a></p>
            <p>Website: <a href="{company_website}">{company_name}</a></p>
        </div>
    </div>
</body>
</html>
"""
