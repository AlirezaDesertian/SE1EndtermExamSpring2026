import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.booking_service import BookingService

class TestBookingServiceUnit(unittest.TestCase):
    def setUp(self):
        self.mock_booking_repo = MagicMock()
        self.mock_property_repo = MagicMock()
        self.service = BookingService(self.mock_booking_repo, self.mock_property_repo)

    def test_create_booking_success(self):
        self.mock_property_repo.get_by_id.return_value = {"id": 1, "is_available": True}
        
        success, message = self.service.create_booking(user_id=101, property_id=1, checkin="2026-06-01", checkout="2026-06-05")
        
        self.assertTrue(success)
        self.assertEqual(message, "Booking successful")
        self.mock_booking_repo.save.assert_called_once()

    def test_create_booking_property_unavailable(self):
        self.mock_property_repo.get_by_id.return_value = {"id": 1, "is_available": False}
        
        success, message = self.service.create_booking(user_id=101, property_id=1, checkin="2026-06-01", checkout="2026-06-05")
        
        self.assertFalse(success)
        self.assertEqual(message, "Property is not available")
        self.mock_booking_repo.save.assert_not_called()