-- Create the Schema of little lemon analysis project
CREATE SCHEMA little_lemon_analysis;

-- Create Customers Table
CREATE TABLE little_lemon_analysis.Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerName VARCHAR(100),
    City VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    CountryCode VARCHAR(10)
);

-- Create Orders Table
CREATE TABLE little_lemon_analysis.Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate DATE,
    DeliveryDate DATE,
    CustomerID INT,
    Cost DECIMAL(10, 2),
    Sales DECIMAL(10, 2),
    Quantity INT,
    Discount DECIMAL(5, 2),
    DeliveryCost DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create MenuItems Table
CREATE TABLE little_lemon_analysis.MenuItems (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,
    CourseName VARCHAR(100),
    CuisineName VARCHAR(100),
    StarterName VARCHAR(100),
    DessertName VARCHAR(100),
    Drink VARCHAR(100),
    Sides VARCHAR(100)
);

-- Create Bookings Table
CREATE TABLE little_lemon_analysis.Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    CustomerID INT,
    MenuItemID INT,
    BookingDate DATE,
    DeliveryDate DATE,
    BookingStatus VARCHAR(20),
    FOREIGN KEY (OrderID) REFERENCES little_lemon_analysis.Orders(OrderID),
    FOREIGN KEY (CustomerID) REFERENCES little_lemon_analysis.Customers(CustomerID),
    FOREIGN KEY (MenuItemID) REFERENCES little_lemon_analysis.MenuItems(ItemID)
);