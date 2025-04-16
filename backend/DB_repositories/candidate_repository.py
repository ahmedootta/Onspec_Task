from candidates.models import Candidate
from rest_framework.exceptions import APIException
class CandidateRepository:

    @staticmethod
    def get_all_candidates():
        return Candidate.objects.all()

    @staticmethod
    def get_candidate_by_id(candidate_id):
        return Candidate.objects.get(id=candidate_id)
    
    @staticmethod
    def get_candidate_by_email(candidate_email):
        return Candidate.objects.filter(email=candidate_email).first()

    @staticmethod
    def create_candidate(validated_fields):
        new_candidate = Candidate(**validated_fields)
        new_candidate.full_clean()
        new_candidate.save()
        return new_candidate
    
    @staticmethod
    def update_candidate(candidate_id, updated_fields):
        updated_candidate = CandidateRepository.get_candidate_by_id(candidate_id) 
        for field, value in updated_fields.items():
            setattr(updated_candidate, field, value)   
        updated_candidate.full_clean()    
        updated_candidate.save()
        return updated_candidate 

    @staticmethod
    def delete_candidate(candidate_id):
        return Candidate.objects.filter(id=candidate_id).delete()                 