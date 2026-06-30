import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.booking_service import BookingService

class FakePropertyRepository:
    def get_by_id(self, property_id):
        if property_id == 1:
            return {"id": 1, "title": "Villa in North", "is_available": True}
        return None

class FakeBookingRepository:
    def __init__(self):
        self.db = []
    def save(self, booking):
        self.db.append(booking)

class TestBookingAcceptance(unittest.TestCase):
    def test_user_can_book_available_property(self):
        prop_repo = FakePropertyRepository()
        book_repo = FakeBookingRepository()
        service = BookingService(book_repo, prop_repo)

        success, message = service.create_booking(user_id=55, property_id=1, checkin="2026-07-10", checkout="2026-07-15")

        self.assertTrue(success)
        self.assertEqual(len(book_repo.db), 1)
        self.assertEqual(book_repo.db[0]["user_id"], 55)