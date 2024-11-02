from rest_framework import serializers

from apps.tour.models import (
    Tour, Program, Duration,
    Included, NotIncluded, Equipment,
    PickupLocations, TourImage, TourDates, Category
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'id', 'title'


class IncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Included
        fields = ('id', 'title')


class NotIncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotIncluded
        fields = ('id', 'title')


class DurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duration
        fields = 'title',


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('title', 'time')


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'title')


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupLocations
        fields = ('id', 'title', 'latitude', 'longitude', )


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = 'image', 'id'


class TourDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDates
        fields = ('id', 'date')


class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, read_only=True)
    pickup_locations = LocationsSerializer(many=True, read_only=True)
    program = ProgramSerializer(many=True, read_only=True)
    equipment = EquipmentSerializer(many=True, read_only=True)
    included = IncludedSerializer(many=True, read_only=True)
    not_included = NotIncludedSerializer(many=True, read_only=True)
    duration = DurationSerializer(read_only=True)
    tour_dates = TourDateSerializer(many=True, read_only=True)
    # tags = TagSerializer(read_only=True)

    class Meta:
        model = Tour
        fields = (
            'id', 'category', 'title',
            'point', 'price', 'images',
            'description', 'pickup_locations',
            'duration', 'difficulty', 'program',
            'equipment', 'included', 'not_included',
            'tour_dates' # 'tags',
        )


class TourCardSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, read_only=True)
    duration = DurationSerializer(read_only=True)
    tour_dates = TourDateSerializer(many=True, read_only=True)
    is_favorite = serializers.BooleanField(read_only=True)

    class Meta:
        model = Tour
        fields = (
            'id', 'images',
            'price', 'title',
            'duration', 'tour_dates',
            'is_favorite'
        )
