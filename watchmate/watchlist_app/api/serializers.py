from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        #fields = "__all__"
        exclude = ('watchlist',)



class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    #watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        

        
        
    # len_name = serializers.SerializerMethodField()

    # def validate_name(self, value): # field level validation
    #     if len(value)<2:
    #         raise serializers.ValidationError("Movie name must be at least 2 characters long")
    #     else:
    #         return value

    # def validate(self, data): # object level validation

    #     if data['name'] == data['descirption']:
    #         raise serializers.ValidationError("Movie name and description must be unique")
    #     else:
    #         return data
    
    # def get_len_name(self, obj):
    #     length = len(obj.name)
    #     return length

        
        





# def name_length( value):
#     if len(value) <= 3:
#         raise serializers.ValidationError('Name must be more than 3 characters')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     descirption = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.descirption = validated_data.get('descirption', instance.descirption)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # def validate_name(self, value): # field level validation
#     #     if len(value)<2:
#     #         raise serializers.ValidationError("Movie name must be at least 2 characters long")
#     #     else:
#     #         return value

#     def validate(self, data): # object level validation

#         if data['name'] == data['descirption']:
#             raise serializers.ValidationError("Movie name and description must be unique")
#         else:
#             return data
        
    





