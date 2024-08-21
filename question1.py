# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        """Update the owner of the vehicle."""
        self.owner = new_owner
        print(f"Owner updated to {new_owner}")

vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Truck", "Jane Smith")

# Print initial owners
print(f"Vehicle 1 (Reg: {vehicle1.registration_number}) is owned by {vehicle1.owner}")
print(f"Vehicle 2 (Reg: {vehicle2.registration_number}) is owned by {vehicle2.owner}")

# Update owners
vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Brown")

# Print updated owners
print(f"Vehicle 1 (Reg: {vehicle1.registration_number}) is now owned by {vehicle1.owner}")
print(f"Vehicle 2 (Reg: {vehicle2.registration_number}) is now owned by {vehicle2.owner}")


# Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0  

    def add_participant(self):
        """Increase the participant count by 1."""
        self.participants += 1
        print(f"Participant added. Total participants: {self.participants}")

    def get_participant_count(self):
        """Return the current participant count."""
        return self.participants

event = Event("City Marathon", "2024-09-01")

# Add participants
event.add_participant()
event.add_participant()

# Retrieve and print the participant count
print(f"Total participants in {event.name}: {event.get_participant_count()}")
