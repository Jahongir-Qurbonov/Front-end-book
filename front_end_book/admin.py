from django.contrib import admin

from front_end_book.models import AttributeExample, Element, ElementAttributes, ElementExample

# Register models

admin.site.register([
    Element,
    ElementExample,
    ElementAttributes,
    AttributeExample,
])
