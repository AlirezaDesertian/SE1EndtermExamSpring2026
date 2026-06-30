class BookingService:
    def __init__(self, booking_repo, property_repo):
        self.booking_repo = booking_repo
        self.property_repo = property_repo

    def create_booking(self, user_id, property_id, checkin, checkout):
        property_data = self.property_repo.get_by_id(property_id)
        
        if not property_data:
            return False, "Property not found"
            
        if not property_data.get('is_available'):
            return False, "Property is not available"

        booking = {
            "user_id": user_id,
            "property_id": property_id,
            "checkin": checkin,
            "checkout": checkout
        }
        self.booking_repo.save(booking)
        return True, "Booking successful"