import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore
from uuid import getnode as get_mac
from time import sleep
import os
mac = str(get_mac())
config={
  "type": "service_account",
  "project_id": "myapp-8b90c",
  "private_key_id": "964fa9f35237a747f3b74479127ff5e73c59155e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC0zOqxTtYxX9Wy\nn6EMmzUl2TL8CMBkzXbrqm1ZWgsQuVAYv82z5+HHnZeO4Lko+oAsJuyBOZsatR9O\n6FTo2kZQVAHQGjXGpmuLR8SJZqzL96sf8OMmEdOd/G1Bea4gKvAvB/RE4EwK3V1Q\nd+J7XOXi9uiBsnU6roQlYkV99baicSDfelIroZ6c21f1R3C3HQIeGN+ewfP/C8T7\nvNW/kRIzHAKztsgHflLAhFuDSuDULGgNyr2H4V5MnFxQgAqvPlLIkx2XV2RUFsV3\n7yLfZLOZA3WHbCOl3VRMbpmpJoCzQ9PyLmPoarst4YPBbiFR6atcVf5a4TcozLix\nSRTJXQDtAgMBAAECggEAFDqDHbBw5ZhP3ArhJXxuD1yESE+gWwbkAc0RK/iXmVjq\nfcJj/Pd6Ou/GZ7176fpRAd+fAXxU/sF6DcWPznexe0ZS55ovHxk6mhw/AJKEzdNZ\niZrVh0piT2BRRwyar02ujsyIh3ZC+8o1qQ2owN2teN3gOLajSBwDe/1JQiUOOJFX\n8cZoFKCnK8mPs8lRNYigd9Abyn9knf1oIXt6T/V9zjCyYozR9vA1SWPSOli1U5r8\nnaha8RmDilyJEKC9/BnVaxcoTRfe/tdYF/YHkfecv8NhwA6UvVxMh00TiPEkdOqG\nKlnFhaQFf/jzciLyULfEdNUFBNZeer1kYxdI2osPHwKBgQD9DDK9YMAAdt1DIy15\nX1ru/0xVC9q9UEki0hw1hxM9loaAbDyirqoLPVsrbHdK0s8FQSUYQz0uGHPn0PoF\nab+KiswbEK7oEnMRLy2q6PpgXE0aHa0d/6mwaombVelhvfuyL+hXrtd3v4V5Dphf\n6FbyyKOSn8OpZYBLbYItp8uUswKBgQC26O5QRkGDdZ7++G9u+kRD8sVc8FL4ABbk\nU6Q6pLGmU/tz0Qt9CiEQESYGK5Es3wRQo7rehvFb1Pt9V8gf4XVNeOHufp9D5jmo\neRI0NsD0UBoabK9NA3h5olTlQcaqGiIXW/IWF0WKwjjwhzcB7Q2Fh9PNi3sBRNkR\n0/q3PIYj3wKBgQCyvmwU84OMkGno469afa3JBpMPvAjuEwkmTI5ajShdJ7eofUwz\nifdZayS8PqjhNJnBV2vxgIV1yxYMWMRTEIiZP0O/loBGM8oOCGpUwK8jY++ek/nW\nJ+LgV9EN5ZiuTzm8ezS+wyU2VBXfFh0yGfdZFbrddncKcEU4goki4NTgGwKBgGfA\nHF2gXEzrDPLnjJ3Qi6RXMqgTEZzmwBVndEJnZPVJsdnx+6hDdJmegIkDcWeYYOQ0\n2yyaMpG6b6SbhELBKj51kQItBL4I+y+a7T58yFpMjWHrwEvY6h9keu9Hrh6SkD/b\nwafSL3oTzSRyLjuDcSYK85MlyPHhUZeRPCdvx07VAoGBAPHzkXoC6GA0E/P4kY9U\nAv77Saq5kiy5fkLIlRWyRzFaxP+WmLloiYNEmwP/S7O1G5KjIBYGyK8jLirHvI0b\nRiAPTo9iptI8qXSe982HFwPGY4KlnHYLpT8kjseHmwLhLNTncLnpJAWeR5AUBvTN\n1m5ZVbNCb9Feqf006OnZuvJZ\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-gq1bh@myapp-8b90c.iam.gserviceaccount.com",
  "client_id": "106356753876247857302",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-gq1bh%40myapp-8b90c.iam.gserviceaccount.com"
}

cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)
db=firestore.client()

def check():
	print("         Approval System")
	print("="*46)
	print("         Your Token :",mac)
	print("="*46)
	print("       Checking Your Approval...")
	chk= db.collection('Users').document(mac).get()
	if chk.exists:
		print("Approved")
		
	else:
		print("Buy Token")
	
check()