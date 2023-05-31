from .base import *
import os
from decouple import config
import dj_database_url

try:
    from .local import *
except ImportError:
    pass
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'
#SECRET_KEY = os.getenv('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': '5432'
    }
}
DATABASES['default'] = dj_database_url.config(conn_max_age=10000, ssl_require=True)

# AWS_S3_ENDPOINT_URL = 'https://spotlightkenya.sgp1.digitaloceanspaces.com'  # Replace your-region with the region where your bucket is located
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_ACCESS_KEY_ID="DO00WBEEMAQWJ4FZCGLX"
# AWS_SECRET_ACCESS_KEY="hx0HQ6vEKqP2eW/AICZcWBCg5JfSQBSPEj8tc+f5ERI"
# AWS_STORAGE_BUCKET_NAME='spotlightkenya'

# AWS_LOCATION = os.getenv("AWS_LOCATION", "static")
# PUBLIC_MEDIA_LOCATION = os.getenv("PUBLIC_MEDIA_LOCATION", "media")
#AWS_DEFAULT_ACL = "public-read"
# AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com"
# AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
# // Import the functions you need from the SDKs you need

# // TODO: Add SDKs for Firebase products that you want to use
# // https://firebase.google.com/docs/web/setup#available-libraries
#
# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
# const firebaseConfig = {
#   apiKey: "AIzaSyCZrkdwVOuegtnwsc-SDYQQ4hiQIs2peQE",
#   authDomain: "spotlightkenya-1596d.firebaseapp.com",
#   projectId: "spotlightkenya-1596d",
#   storageBucket: "spotlightkenya-1596d.appspot.com",
#   messagingSenderId: "83044048851",
#   appId: "1:83044048851:web:6a727b359eefce681fd926",
#   measurementId: "G-PXKLX27W4K"
