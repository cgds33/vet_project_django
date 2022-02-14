from django.test import TestCase


# Create your tests here.


# URL patterns test
class URLTest(TestCase):
    def testIndex(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200) # Does it give the result of "HTTP 200 OK"? 

    def testPets(self):
        response = self.client.get("/pets/allpets/")
        self.assertEqual(response.status_code,200)

    def testUsers(self):
        response = self.client.get("/user/users/")
        self.assertEqual(response.status_code,200)

    def testObjectives(self):
        response = self.client.get("/objectives/")
        self.assertEqual(response.status_code,200)

    def testAbout(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code,200)

    def testLogin(self):
        response = self.client.get("/user/login/")
        self.assertEqual(response.status_code,200)

    def testRegister(self):
        response = self.client.get("/user/register/")
        self.assertEqual(response.status_code,200)









