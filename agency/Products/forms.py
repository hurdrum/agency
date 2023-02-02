

from django.forms import BaseForm


class addFavorite(BaseForm):
    class Meta:
        fields = ['product_id',]

