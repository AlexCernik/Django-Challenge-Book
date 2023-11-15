from rest_framework import serializers
from datetime import date
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'year_publication'
        )
        
    def validate_author(self, value):
        if not all(value.isalpha() or value.isspace() for value in value):
            raise serializers.ValidationError('Verifica la composición del nombre del autor.')
        return value

    def validate_year_publication(self, value):
        if value > date.today():
            raise serializers.ValidationError('La fecha de publicación no puede ser mayor a la fecha acual.')
        return value