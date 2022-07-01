from django.test import TestCase
from utilities import fraud_detector, service_classifier


class UtilsTestClass(TestCase):

    def test_fraud_detector(self):
        res = fraud_detector.fraud_detector('test')
        self.assertGreaterEqual(res, 0)
        self.assertLessEqual(res, 1)

    def test_service_classifier(self):
        res = service_classifier.service_classifier('test')
        self.assertIsInstance(res, dict)
