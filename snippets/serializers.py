from rest_framework import serializers

from snippets.models import Tag, Snippets


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "title"]
        extra_kwargs = {
            'title': {'validators': []}
        }


class SnippetsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Snippets
        fields = [
            "id", "title", "note", "tags", "created_at", "updated_at"
        ]

    def create(self, validated_data):
        tag_data = validated_data.pop('tags', [])
        snippet = Snippets.objects.create(**validated_data)

        snippet.tags.add(*[
            Tag.objects.get_or_create(
                title=tag.get('title', '').strip().lower()
            )[0]
            for tag in tag_data
        ])
        return snippet

    def update(self, instance, validated_data):
        tag_data = validated_data.pop('tags', None)

        for attr, values in validated_data.items():
            setattr(instance, attr, values)

        if tag_data is not None:
            instance.tags.clear()
            tag_li = [
                Tag.objects.get_or_create(
                    title=tag.get('title', '').strip().lower()
                )[0]
                for tag in tag_data
            ]
            instance.tags.set(tag_li)
        instance.save()
        return instance


class SnippetsOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = [
            "id", "title", "note", "created_at", "updated_at"
        ]
