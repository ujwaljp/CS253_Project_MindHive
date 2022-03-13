from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TockenGenerator(PasswordResetTokenGenerator):
    
    def hash(self, user, timestamp):
        return six.text_type(str(user.id)+str(timestamp))

generate_token = TockenGenerator()