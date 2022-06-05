from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Birmingham_Vibe_Serializer
from .models import Birmingham_Vibe_library


@api_view(['GET'])
def birmingham_vibe_list(request):
    
    birmingham_vibe_library = Birmingham_Vibe_library.objects.all()
    serializer = Birmingham_Vibe_Serializer(birmingham_vibe_library, many=True)

    print(serializer.data)
    return Response(serializer.data)