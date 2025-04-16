from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Candidate
from datetime import time

# Create your tests here.

class CandidateCreateUpdateTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create_update') 
        self.valid_data = {
            "first_name": "Ahmed",
            "last_name": "Fadl",
            "email": "ahmed@example.com",
            "phone_number": "01012345678",
            "preferred_time_start": "10:00:00",
            "preferred_time_end": "15:00:00",
            "linkedIn": "https://linkedin.com/in/ahmedfadl",
            "github": "https://github.com/ahmedfadl",
            "comment": "Very enthusiastic about backend development." 
        }
    # Happy scenario of creation   
    def test_create_candidate(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), 1)
        self.assertEqual(Candidate.objects.first().email, "ahmed@example.com")
    
    # Update last_name & comment & time interval for existing email.
    def test_update_candidate(self):
        updated_data = {
            "first_name": "Ahmed",
            "last_name": "Updated",
            "email": "ahmed.fadl@example.com", 
            "phone_number": "01012345678",
            "preferred_time_start": "13:00:00",
            "preferred_time_end": "17:00:00",
            "linkedIn": "https://linkedin.com/in/ahmedfadl",
            "github": "https://github.com/ahmedfadl",
            "comment": "Eager to show my skills in backend development." 
        }
        response = self.client.post(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), 1)
        self.assertEqual(Candidate.objects.first().last_name, "Updated")
        self.assertEqual(Candidate.objects.first().preferred_time_start, time(13, 0, 0))
        self.assertEqual(Candidate.objects.first().preferred_time_end, time(17, 0, 0))
        self.assertEqual(Candidate.objects.first().comment, "Eager to show my skills in backend development.")

    # Test missing of all required feilds
    def test_missing_fields(self):
        incomplete_data = {
            "email": "ahmednew@example.com",
            "phone_number": "01111111111"
        }
        response = self.client.post(self.url, incomplete_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_missing_fields = [
            "first_name", 
            "last_name", 
            "preferred_time_start", 
            "preferred_time_end", 
            "linkedIn", 
            "github",
            "comment"
        ]
        for field in expected_missing_fields:
            self.assertIn(field, response.data)

    # Test email of candidate
    def test_invalid_email_format(self):
        invalid_data = {
            "first_name": "Mona",
            "last_name": "Saleh",
            "email": "not-an-email",
            "phone": "01012345678",
            "preferred_time_start": "09:30:00",
            "preferred_time_end": "13:00:00",
            "linkedIn": "https://linkedin.com/in/monasaleh",
            "github": "https://github.com/monasaleh",
            "comment": "Loves working with Django and PostgreSQL."
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    # Test phone_number format
    def test_invalid_egyptian_phone_format(self):
        invalid_data = {
            "first_name": "Youssef",
            "last_name": "Kamel",
            "slug": "youssef-kamel",
            "email": "youssef.kamel@example.com",
            "phone_number": "03555667788",
            "preferred_time_start": "11:00:00",
            "preferred_time_end": "16:00:00",
            "linkedIn": "https://linkedin.com/in/youssefkamel",
            "github": "https://github.com/youssefkamel",
            "comment": "Wants to grow in cloud-native and CI/CD workflows."
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("phone_number", response.data)

    # Test linkedin & github urls
    def test_invalid_url_format(self):
        invalid_data = {
            "first_name": "Youssef",
            "last_name": "Kamel",
            "email": "youssef.kamel@example.com",
            "phone_number": "01555667788",
            "preferred_time_start": "11:00:00",
            "preferred_time_end": "16:00:00",
            "linkedIn": "https://github.com/in/youssefkamel",
            "github": "https://linkedin.com/youssefkamel",
            "comment": "Wants to grow in cloud-native and CI/CD workflows."
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        for field in ["linkedIn", "github"]:
            self.assertIn(field, response.data) 

    # Test preferred time for calling (end > start)
    def test_invalid_time_interval(self):
        invalid_data = {
            "first_name": "Maher",
            "last_name": "Osman",
            "email": "Maher.Osman@example.com",
            "phone_number": "01555667788",
            "preferred_time_start": "11:00:00",
            "preferred_time_end": "10:00:00",
            "linkedIn": "https://linkedin.com/MaherOsman",
            "github": "https://github.com/in/MaherOsman",
            "comment": "Wants to grow in Devops."
        }  
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Time", response.data)         