This is a storefront app for the MeanMugs business.

It should have:

ROUTES:
- products
- products/<product_id>
- cart
- signup
- signin

DATABASE TABLES:
- User (user_id, username, password, email)
- Product (product_id, name, description, price, image, quantity)
- Cart (cart_id, user_id (FK), product_id (FK))

FUNCTIONALITY:
- A user should be able to sign up
- A route that shows a list of all available products
- When you click on a product it should be able to link to a route which shows a single product (with the information of the product you just clicked)
- User should be able to add a product to their cart, but only if they are logged in
- A route (cart) that shows a list of products you’ve added into your cart as well as the total of all the items in your cart
- Add a route that, when clicked handles functionality that removes all items from your cart one time. Also create a button that, when pressed, it removes that specific product object from the cart.