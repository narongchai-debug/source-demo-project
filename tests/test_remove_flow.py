from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.header_page import HeaderPage

def test_remove_flow(logged_in_driver, selected_products):
    #add product to cart
    product_page = ProductPage(logged_in_driver)


    for add_product in selected_products:
        product_page.addToCart(add_product)
    #remove product from cart   
    cart_page =  CartPage(logged_in_driver)

    for remove_product in selected_products :
        cart_page.removeItems(remove_product)
    
    header_page = HeaderPage(logged_in_driver) 
    header_page.logout()