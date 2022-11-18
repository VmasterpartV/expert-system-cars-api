from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        response = data.get('response')
        reason = data.get('reason')
        image = data.get('image')
        options = data.get('options')
        if type(options) == str:
            options = options.split(',')
        print(options)
        car = Car.objects.create(response=response, reason=reason, image=image)
        for option in options:
            car.options.add(option)
        car.save()
        serializer = CarSerializer(car)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def find_car(self, request, *args, **kwargs):
        data = request.data
        options = data.get('options')
        options = Option.objects.filter(id__in=options)
        cars = Car.objects.filter(options__id__in=options)
        if cars.exists():
            for car in cars:
                if set(car.options.all()) == set(options.all()):
                    serializer = CarSerializer(car)
                    return Response(serializer.data)
        return Response({'message': 'No car found'})
        