class BookingService:

    def __init__(self, booking_repo, property_repo):
        self.booking_repo = booking_repo
        self.property_repo = property_repo

    def create_booking(self, user_id, property_id, checkin, checkout):
        pass