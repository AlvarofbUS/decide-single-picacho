from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from base import mods


class PostProcTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)

    def tearDown(self):
        self.client = None

    def test_identity(self):
        data = {
            'type': 'IDENTITY',
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 5 },
                { 'option': 'Option 2', 'number': 2, 'votes': 0 },
                { 'option': 'Option 3', 'number': 3, 'votes': 3 },
                { 'option': 'Option 4', 'number': 4, 'votes': 2 },
                { 'option': 'Option 5', 'number': 5, 'votes': 5 },
                { 'option': 'Option 6', 'number': 6, 'votes': 1 },
            ]
        }

        expected_result = [
            { 'option': 'Option 1', 'number': 1, 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 5', 'number': 5, 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 3', 'number': 3, 'votes': 3, 'postproc': 3 },
            { 'option': 'Option 4', 'number': 4, 'votes': 2, 'postproc': 2 },
            { 'option': 'Option 6', 'number': 6, 'votes': 1, 'postproc': 1 },
            { 'option': 'Option 2', 'number': 2, 'votes': 0, 'postproc': 0 },
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)
        
    def test_leydhont(self):
        data = {
            'type': 'DHONDT',
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 1},
                { 'option': 'Option 2', 'number': 2, 'votes': 1},
            ],
            'escanio':5,
        }

        expected_result = [
            { 'votes': 1,'number': 1, 'option': 'Option 1', 'escanio': 3 },
            { 'votes': 1,'number': 2, 'option': 'Option 2', 'escanio': 2 },
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)
    
    def test_leydhont2(self):
        data = {
            'type': 'DHONDT',
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 340000},
                { 'option': 'Option 2', 'number': 2, 'votes': 280000},
                { 'option': 'Option 3', 'number': 3, 'votes': 160000},
                { 'option': 'Option 4', 'number': 4, 'votes': 60000},
                { 'option': 'Option 5', 'number': 5, 'votes': 15000},
            ],
            'escanio':7,
        }

        expected_result = [
            { 'votes': 340000,'number': 1, 'option': 'Option 1', 'escanio': 3 },
            { 'votes': 280000,'number': 2, 'option': 'Option 2', 'escanio': 3 },
            { 'votes': 160000,'number': 3, 'option': 'Option 3', 'escanio': 1 },
            { 'votes': 60000,'number': 4, 'option': 'Option 4', 'escanio': 0 },
            { 'votes': 15000,'number': 5, 'option': 'Option 5', 'escanio': 0 },
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)
    
    def test_simple(self):
        data = {
            'type': 'SIMPLE',
            'escanio':30,
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 15 },
                { 'option': 'Option 2', 'number': 2, 'votes': 10 },
                { 'option': 'Option 3', 'number': 3, 'votes': 14},
                { 'option': 'Option 4', 'number': 4, 'votes': 5},
                { 'option': 'Option 5', 'number': 5, 'votes': 2 },
                { 'option': 'Option 6', 'number': 6, 'votes': 1},
            ]
        }
        expected_result = [
            { 'option': 'Option 1', 'number': 1, 'votes': 15, 'escanio':  10},
            { 'option': 'Option 3', 'number': 3, 'votes': 14, 'escanio':  9},
            { 'option': 'Option 2', 'number': 2, 'votes': 10, 'escanio': 6},
            { 'option': 'Option 4', 'number': 4, 'votes': 5, 'escanio': 3},
            { 'option': 'Option 5', 'number': 5, 'votes': 2, 'escanio': 1},
            { 'option': 'Option 6', 'number': 6, 'votes': 1, 'escanio': 1},
        ]
        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)

    def test_simple2(self):
        data = {
            'type': 'SIMPLE',
            'escanio':70,
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 50 },
                { 'option': 'Option 2', 'number': 2, 'votes': 11 },
                { 'option': 'Option 3', 'number': 3, 'votes': 10},
                { 'option': 'Option 4', 'number': 4, 'votes': 1 },
                { 'option': 'Option 5', 'number': 5, 'votes': 6 },
                { 'option': 'Option 6', 'number': 6, 'votes': 4 },
            ]
        }
        expected_result = [
            { 'option': 'Option 1', 'number': 1, 'votes': 50, 'escanio':  43},
            { 'option': 'Option 2', 'number': 2, 'votes': 11, 'escanio':  9},
            { 'option': 'Option 3', 'number': 3, 'votes': 10, 'escanio': 9},
            { 'option': 'Option 5', 'number': 5, 'votes': 6, 'escanio': 5},
            { 'option': 'Option 6', 'number': 6, 'votes': 4, 'escanio': 3},
            { 'option': 'Option 4', 'number': 4, 'votes': 1, 'escanio': 1},
        ]
        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)
    
    def test_simple3(self):
        data = {
            'type': 'SIMPLE',
            'escanio':30,
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 15 },
                { 'option': 'Option 2', 'number': 2, 'votes': 10 },
                { 'option': 'Option 3', 'number': 3, 'votes': 14},
                { 'option': 'Option 4', 'number': 4, 'votes': 5},
                { 'option': 'Option 5', 'number': 5, 'votes': 2 },
                { 'option': 'Option 6', 'number': 6, 'votes': 1},
            ]
        }
        expected_result = [
            { 'option': 'Option 1', 'number': 1, 'votes': 15, 'escanio':  10},
            { 'option': 'Option 3', 'number': 3, 'votes': 14, 'escanio':  9},
            { 'option': 'Option 2', 'number': 2, 'votes': 10, 'escanio': 6},
            { 'option': 'Option 4', 'number': 4, 'votes': 5, 'escanio': 3},
            { 'option': 'Option 5', 'number': 5, 'votes': 2, 'escanio': 1},
            { 'option': 'Option 6', 'number': 6, 'votes': 1, 'escanio': 1},
        ]
        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)