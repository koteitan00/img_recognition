from google_drive_ocr.application import GoogleOCRApplication

app = GoogleOCRApplication(r'C:\Users\user_\test\client_secret.json')

app.perform_ocr(r'C:\Users\user_\test\test.png')
