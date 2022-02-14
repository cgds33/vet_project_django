from django.test import TestCase
from django.contrib.auth.models import User
from pets.models import Pet

# Create your tests here.

# Tester class whether the model works 
class modelsTesting(TestCase):
    def setUp(self):
        testUser = User.objects.create_user(
            username="testuser",password="123456"
        )

        self.petName = Pet.objects.create(
            author = testUser, petName = "testPetName",
            petType = "testPetType", petSpecies ="testPetSpecies",
            petAge = "1", content = "TestContent"
        )

    # Starts with test code
    def testModelStr(self):
        self.assertEqual(self.petName.petName,"testPetName")


