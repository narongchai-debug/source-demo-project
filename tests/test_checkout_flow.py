from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.header_page import HeaderPage

def test_checkout_flow(logged_in_driver, selected_products):
    #Login
    product_page = ProductPage(logged_in_driver)
    #Add to cart
    for selected_product in selected_products:
        product_page.addToCart(selected_product)

    #Checkout 
    cart_page = CartPage(logged_in_driver)
    cart_page.checkOutItems("Mr.bean", "booboo", 10400)

    #Logout
    header_page = HeaderPage(logged_in_driver)
    header_page.logout()
