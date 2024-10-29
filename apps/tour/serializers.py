from rest_framework import serializers

from apps.tour.models import Tour


class TourSerializer(serializers.ModelSerializer):
    # images = TourImageSerializer(many=True, read_only=True)
    # pickup_locations = LocationsSerializer(many=True, read_only=True)
    # program = ProgramSerializer(many=True, read_only=True)
    # equipment = EquipmentSerializer(many=True, read_only=True)
    # included = IncludedSerializer(many=True, read_only=True)
    # not_included = NotIncludedSerializer(many=True, read_only=True)
    # difficulty = DifficultySerializer(read_only=True)
    # tags = TagSerializer(read_only=True)
    # tour_dates = TourDateSerializer(many=True, read_only=True)
    # duration = DurationSerializer(read_only=True)

    class Meta:
        model = Tour
        fields = (
            'id',
            # 'category',
            'title',
            # 'region_country', 'price', 'images',
            # 'description', 'pickup_locations', 'duration',
            # 'difficulty', 'program', 'equipment',
            # 'included', 'not_included', 'tags',
            # 'tour_dates'
        )
