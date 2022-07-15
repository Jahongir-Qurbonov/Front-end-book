from django.db import models

# Models

class Element(models.Model):
    name = models.CharField(max_length=15)
    information = models.TextField()
    
    collections = [
        ('base', 'base'),
        ('forms', 'forms'),
        ('lists', 'lists'),
        ('semantic', 'semantic'),
        ('tables', 'tables'),
    ]
    collection = models.CharField(max_length=10, choices=collections, blank=True, null=True)

    experimental = models.BooleanField(default=False)
    meta = models.BooleanField(default=False)
    self_closing = models.BooleanField(default=False)
    inline = models.BooleanField(default=False)
    block = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'


class ElementExample(models.Model):
    example_code = models.TextField()

    element = models.ForeignKey(Element, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.element.name} element example code'


class ElementAttributes(models.Model):
    name = models.CharField(max_length=15)
    information = models.TextField()

    required = models.BooleanField()

    element = models.ForeignKey(Element, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - attribute of a <{self.element.name}> element"


class AttributeExample(models.Model):
    example = models.TextField()
    information = models.TextField()

    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    attribute = models.ForeignKey(ElementAttributes, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.example}. Belongs to the {self.element.name} element. ({self.attribute.name})'
