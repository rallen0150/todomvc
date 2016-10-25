from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        def get_completed(self):
            return getattr(completed=True)

        model = Todo
        fields = '__all__'
