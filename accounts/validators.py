from django.core.exceptions import ValidationError
import os

def allow_only_image_validator(value):
    ext = os.path.splitext(value.name)[1] #cover-image.jpg jpg is extension(ext)
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('unsupported file extension. Allowed extensions: ' +str(valid_extensions))