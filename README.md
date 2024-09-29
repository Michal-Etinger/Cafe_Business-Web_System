# Online Cafe Web Order System
Michal Etinger
## Project Overview
The Online Cafe Order System is designed to streamline the ordering and management process for Cafe. This web application allows users to browse the menu, add items to their cart, place orders, and make payments. The system is built with a React frontend and a Flask backend, with data stored in a SQLite database.

## Project Purpose and General Explanation
The primary goal of this project is to provide a seamless and efficient ordering experience for both customers and cafe staff. The application supports various functionalities including user authentication, order management, and real-time menu updates.

## User Types
1. **Customers**: 
   - Browse the menu
   - Add items to their cart
   - Place orders
   - Make payments
   - Leave reviews and ratings

2. **Cafe Staff**:
   - Manage menu items
   - View and process orders
   - Update order statuses
   - Analyze order statistics

## Processes
1. **User Registration and Login**:
   - Users can sign up and log in to access personalized features.
   
2. **Browsing the Menu**:
   - Customers can view various categories of menu items including burgers, breakfast items, shakes, and hotdogs.
   
3. **Adding Items to Cart**:
   - Customers can add selected items to their shopping cart for review before placing an order.
   
4. **Placing Orders**:
   - Customers can place orders by confirming their cart items and proceeding to payment.
   
5. **Order Management**:
   - Restaurant staff can view incoming orders, update their status, and manage order details.

## Managed Data
The system manages the following data:
1. **Users**:
   - Username
   - Password (hashed)
   - User roles (customer or staff)

2. **Menu Items**:
   - Item ID
   - Item name
   - Item type (category)
   - Item price

3. **Orders**:
   - Order ID
   - Client ID
   - Order products
   - Total price
   - Order status
   - Order review
   - Order rating

## Overall Architecture
The architecture of the Online Restaurant Order System is based on a client-server model:
- **Frontend**: Developed using React, it handles the user interface and interactions.
- **Backend**: Developed using Flask, it processes requests, manages the database, and handles business logic.
- **Database**: SQLite is used to store user, menu, and order data.

### Architecture Diagram
