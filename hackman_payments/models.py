from django.conf import settings
from django.db import models


class PaymentTag(models.Model):
    """Map tags in git payment repo to users"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    hashtag = models.CharField(max_length=20, db_index=True, default='dues')
    tag = models.CharField(max_length=50,
                           db_index=True,
                           null=False,
                           blank=True)

    def make_key(self):  # pragma: no cover
        if self.tag:
            return '{}:{}'.format(self.hashtag, self.tag)
        else:
            return self.hashtag
