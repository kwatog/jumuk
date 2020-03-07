import os
from django.contrib.auth import get_user_model
from drf_firebase.authentication import BaseFirebaseAuthentication
from firebase_admin import credentials, initialize_app

FIREBASE_CRED=os.environ.get('DJANGO_MKT_FIREBASE','mkt_firebase.json')

creds = credentials.Certificate(FIREBASE_CRED)
app = initialize_app(creds, name='filipinoSGMarket')


class FirebaseAuthentication(BaseFirebaseAuthentication):
    keyword = 'JWT'

    def get_firebase_app(self):
        return app

    def get_django_user(self, firebase_user_record):
        try:
            # print('hey, ja!')
            print(firebase_user_record.uid)
            return get_user_model().objects.get(firebase_uid=firebase_user_record.uid)
        except get_user_model().DoesNotExist:
            # filtered_username = firebase_user_record.display_name.replace(r'\w', '')
            return get_user_model().objects.create(firebase_uid=firebase_user_record.uid,
                                                   # username=filtered_username,
                                                   email=firebase_user_record.email,
                                                   phone=firebase_user_record.phone_number,
                                                   email_verified=firebase_user_record.email_verified,
                                                   photo_url=firebase_user_record.photo_url
                                                   )
            # return get_user_model().objects.create(firebase_uid=firebase_user_record.uid)
