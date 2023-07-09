from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.
def index(requests):
    return render(requests, "index.html")
    
def index2(requests):
    return render(requests, "index-2.html")
    
def index3(requests):
    return render(requests, "index-3.html")
    
def index4(requests):
    return render(requests, "index-4.html")
    
def index5(requests):
    return render(requests, "index-5.html")

def profile(requests):
    return render(requests, "profile.html")

def wishlist(requests):
    return render(requests, "wishlist.html")
    
def compare(requests):
    return render(requests, "compare.html")
    
def shop(requests):
    return render(requests, "shop.html")
    
def contact(requests):
    return render(requests, "contact.html")
    
def shop_category(requests):
    return render(requests, "shop-category.html")
    
def shop_list(requests):
    return render(requests, "shop-list.html")
    
def error(requests):
    return render(requests, "404.html")
    
def about(requests):
    return render(requests, "about.html")
    
def blog_details(requests):
    return render(requests, "blog-details.html")
    
def blog_details2(requests):
    return render(requests, "blog-details2.html")
    
def blog_grid(requests):
    return render(requests, "blog-grid.html")
    
def blog(requests):
    return render(requests, "blog.html")
    
def cart(requests):
    return render(requests, "cart.html")
    
def checkout(requests):
    return render(requests, "checkout.html")
    
def coupon(requests):
    return render(requests, "coupon.html")
    
def forgot(requests):
    return render(requests, "forgot.html")
    
def order(requests):
    return render(requests, "order.html")
    
def product_details_countdown(requests):
    return render(requests, "product-details-countdown.html")
    
def product_details_gallery(requests):
    return render(requests, "product-details-gallery.html")
    
def product_details_list(requests):
    return render(requests, "product-details-list.html")

def product_details_presentation(requests):
    return render(requests, "product-details-presentation.html")
    
def product_details_progress(requests):
    return render(requests, "product-details-progress.html")
    
def product_details_swatches(requests):
    return render(requests, "product-details-swatches.html")
    
def product_details_slider(requests):
    return render(requests, "product-details-slider.html")
    
def product_details_video(requests):
    return render(requests, "product-details-video.html")
    
def product_details(requests):
    return render(requests, "product-details.html")
    
def shop_1600(requests):
    return render(requests, "shop-1600.html")

def shop_filter_dropdown(requests):
    return render(requests, "shop-filter-dropwdown.html")
    
def shop_filter_offcanvas(requests):
    return render(requests, "shop-filter-offcanvas.html")

def shop_full_width(requests):
    return render(requests, "shop-full-width.html")
    
def shop_infinite_scroll(requests):
    return render(requests, "shop-infinite-scroll.html")

def shop_load_more(requests):
    return render(requests, "shop-load-more.html")
    
def shop_no_sidebar(requests):
    return render(requests, "shop-no-sidebar.html")

def shop_masonary(requests):
    return render(requests, "shop-masonary.html")
    
def shop_right_sidebar(requests):
    return render(requests, "shop-right-sidebar.html")