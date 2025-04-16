from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Candidate
from .serializers import CandidateSerializer
from DB_repositories.candidate_repository import CandidateRepository

# Create your views here.
class CandidateListView(APIView):
    def get(self, request):
        all_candidates = CandidateRepository.get_all_candidates()
        serialized_data = CandidateSerializer(all_candidates, many=True) # convert DB_object to JSON format
        return Response({"All_Candidates": serialized_data.data}, status=status.HTTP_200_OK)
    
class CandidateCreateUpdate(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        candidate_email = serializer.validated_data.get('email')
        existing_candidate = Candidate.objects.filter(email=candidate_email).first()

        if existing_candidate:
            # Update the existing candidate with the submitted data
            CandidateRepository.update_candidate(existing_candidate.id, serializer.validated_data)
            return Response({
                "message": "Candidate updated successfully!",
                "candidate": CandidateSerializer(existing_candidate).data
            }, status=status.HTTP_200_OK)

        else:  # If the email doesn't exist, create a new candidate
            new_candidate = CandidateRepository.create_candidate(serializer.validated_data)
            return Response({
                "message": "Candidate created successfully!",
                "candidate": CandidateSerializer(new_candidate).data
            }, status=status.HTTP_201_CREATED)
        
            






# class CandidateCreate(APIView):
#     def post(self, request):
#         serializer = CandidateSerializer(data=request.data) 
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#         candidate = CandidateRepository.create_candidate(serializer.validated_data)
#         return Response ({
#             "Message": "Candidate added successfully!",
#             "Candidate_id": candidate.id
#         }, status=status.HTTP_201_CREATED) 

# class CandidateUpdate(APIView):
#     def put(self, request, candidate_id):
#         updated_fields = request.data
#         try:
#             updated_candidate = CandidateRepository.update_candidate(candidate_id, updated_fields)
#             return Response({
#                 "Message": "Candidate updated successfully!",
#                 "Updated Candidate": CandidateSerializer(updated_candidate).data
#             }, status=status.HTTP_200_OK)
        
#         except Candidate.DoesNotExist as err:
#             raise NotFound(str(err))      