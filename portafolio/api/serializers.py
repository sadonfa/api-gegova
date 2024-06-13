from rest_framework.serializers import ModelSerializer
from portafolio.models import Portafolio, Categories, Lenguajes

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'description']

class LenguajeSerializer(ModelSerializer):
    class Meta:
        model = Lenguajes
        fields = ['id', 'name']

        print(Lenguajes)

class PortafolioSerializer(ModelSerializer):
    category_data = CategoriesSerializer(source='categories', many=False, read_only=True)
    lenguaje_data = LenguajeSerializer(source='lenguajes', many=True, read_only=True)

    class Meta:
        model = Portafolio
        fields = ['id', 'name', 'categories', 'lenguajes', 'image', 'category_data', 'lenguaje_data']
