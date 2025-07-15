from rest_framework import serializers
from .models import Wired
import requests
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from datetime import date


class WiredSerializer(serializers.ModelSerializer):
  image_url = serializers.URLField(write_only=True,)

  def validate_image_url(self, value):
    if not value:
      return None
    try:
      response = requests.get(value, timeout=5)
      response.raise_for_status()

      content_type = response.headers.get('Content-Type', '')
      if content_type not in ['image/jpeg', 'image/png']:
          raise serializers.ValidationError("Only JPEG and PNG images are allowed.")

      image = Image.open(BytesIO(response.content))
      image.verify()

      image = Image.open(BytesIO(response.content))
      if image.width > 3000 or image.height > 3000:
          raise serializers.ValidationError("Image dimensions should not exceed 3000x3000px.")

    except requests.RequestException:
        raise serializers.ValidationError("Unable to fetch image from the URL.")
    except (Image.DecompressionBombError, Image.UnidentifiedImageError):
        raise serializers.ValidationError("The URL does not point to a valid image.")

    return value
  
  def create(self, validated_data):
    image_url = validated_data.pop('image_url', None)
    if image_url:
      response = requests.get(image_url)
      image_name = image_url.split('/')[-1].split('?')[0]

      image_file = ContentFile(response.content)
      instance = Wired(**validated_data)
      instance.picture.save(image_name, image_file, save=True)

    return instance

  class Meta:
    model = Wired
    fields = ['index', 'title', 'URL', 'image_url', 'date_of_publish', 'picture']