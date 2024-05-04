import mysql.connector

class BookingSystem:
    def __init__(self, host, user, password, database):
        self.db_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db_connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.db_connection.close()

    def GetMaxQuantity(self):
        try:
            query = "SELECT MAX(Quantity) FROM Orders"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result[0]
        except mysql.connector.Error as error:
            print("Error retrieving max quantity:", error)
            return None

    def ManageBooking(self, booking_id, new_status):
        try:
            query = "UPDATE Bookings SET BookingStatus = %s WHERE BookingID = %s"
            self.cursor.execute(query, (new_status, booking_id))
            self.db_connection.commit()
            print("Booking status updated successfully.")
        except mysql.connector.Error as error:
            print("Error updating booking status:", error)

    def UpdateBooking(self, booking_id, new_booking_date, new_delivery_date):
        try:
            query = "UPDATE Bookings SET BookingDate = %s, DeliveryDate = %s WHERE BookingID = %s"
            self.cursor.execute(query, (new_booking_date, new_delivery_date, booking_id))
            self.db_connection.commit()
            print("Booking updated successfully.")
        except mysql.connector.Error as error:
            print("Error updating booking:", error)

    def AddBooking(self, order_id, customer_id, booking_date, delivery_date, booking_status, menu_item_id):
        try:
            query = "INSERT INTO Bookings (OrderID, CustomerID, BookingDate, DeliveryDate, BookingStatus, MenuItemID) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (order_id, customer_id, booking_date, delivery_date, booking_status, menu_item_id))
            self.db_connection.commit()
            print("Booking added successfully.")
        except mysql.connector.Error as error:
            print("Error adding booking:", error)

    def CancelBooking(self, booking_id):
        try:
            query = "DELETE FROM Bookings WHERE BookingID = %s"
            self.cursor.execute(query, (booking_id,))
            self.db_connection.commit()
            print("Booking cancelled successfully.")
        except mysql.connector.Error as error:
            print("Error cancelling booking:", error)

# Example Usage
if __name__ == "__main__":
    # Replace these values with your MySQL connection details
    host = "localhost"
    user = "your_username"
    password = "your_password"
    database = "your_database_name"

    booking_system = BookingSystem(host, user, password, database)

    # Example usage of functions
    max_quantity = booking_system.GetMaxQuantity()
    print("Max Quantity:", max_quantity)

    # Manage a booking by updating its status
    booking_system.ManageBooking(booking_id=1, new_status="confirmed")

    # Update booking details
    booking_system.UpdateBooking(booking_id=1, new_booking_date="2024-05-10", new_delivery_date="2024-05-12")

    # Add a new booking
    booking_system.AddBooking(order_id=1, customer_id=1, booking_date="2024-05-08", delivery_date="2024-05-10", booking_status="pending", menu_item_id=1)

    # Cancel a booking
    booking_system.CancelBooking(booking_id=2)
