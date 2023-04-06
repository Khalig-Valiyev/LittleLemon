from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menu,Booking
from .serializers import bookingSerializer,menuSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def index(request):
    return render(request, 'index.html', {})

class menuView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = menuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status' : 'success', 'data' : serializer.data})
    
    def get(self,request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    
    def handle_no_permission(self):
        return Response({"message": "You must be authenticated to access this endpoint"}, status=401)


class bookingView(APIView):
    def get(self,request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
        
        
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer