from rest_framework import serializers

class NameListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title

class SongListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title