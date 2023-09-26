from django.db import models
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField
from string import hexdigits
from django.utils.html import mark_safe
from vendors.models import Vendor
from customer.models import CustomUser


def product_directory_path(instance, filename):
    return f"vendor_{instance.vend_id}/{filename}"

# product
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="product-", alphabet=hexdigits)
    title = models.CharField(max_length=100)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specifications = models.TextField(null=True, blank=True)


    """
        # Foreign Keys / Table Relationships
    """
    # category
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # inventory
    inventory = models.ForeignKey('Inventory', on_delete=models.SET_NULL, null=True)
    # discount
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return self.title

# product image
class Image(models.Model):
    img_id = ShortUUIDField(unique=True, length=10, max_length=20, alphabet=hexdigits, prefix="image-")
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=product_directory_path)
    
    def image_url(self):
        return mark_safe('<img src="%s" width=50 heigh=50 />', (self.image.url))
    
    class Meta:
        verbose_name_plural = "Images"


class Category(models.Model):
    cat_id = ShortUUIDField(unique=True, length=10, max_length=20, alphabet=hexdigits, prefix="cat-")
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    updated_at = timezone.now()
    created_at = models.DateTimeField(timezone.now())

    class Meta:
        verbose_name_plural = "Categories"

    def __repr__(self):
        return self.name
    
# product inventory
class Inventory(models.Model):
    inv_id = ShortUUIDField(unique=True, length=10, max_length=15, alphabet=hexdigits, prefix="inv-")
    quantity = models.PositiveIntegerField(default=0)
    updated_at = timezone.now()
    created_at = models.DateTimeField(timezone.now())

    class Meta:
        verbose_name_plural = "Inventories"

    def __repr__(self):
        return self.quantity
    
# product discount
class Discount(models.Model):
    dis_id = ShortUUIDField(unique=True, length=10, max_length=15, alphabet=hexdigits, prefix="dis-")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    discount_percent = models.DecimalField(decimal_places=2, max_digits=2)
    active = models.BooleanField(default=False)
    updated_at = timezone.now()
    created_at = models.DateTimeField(timezone.now())

    class Meta:
        verbose_name_plural = "Discounts"

    def __repr__(self):
        return self.name
    

# Cart Item
class CartItem(models.Model):
    cart_id = ShortUUIDField(unique=True, length=10, max_length=15, alphabet=hexdigits, prefix="cart-")
    quantity = models.PositiveIntegerField(default=0)
    updated_at = timezone.now()
    created_at = models.DateTimeField(timezone.now())
    session_id = models.ForeignKey('ShoppingSession', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Cart Items"

    def totalBill(self):
        """
            Return the total amount of all items available in the cart
        """
        pass

    def __repr__(self):
        return self.quantity
    
# user shopping session
class ShoppingSession(models.Model):
    sess_id = ShortUUIDField(unique=True, length=10, max_length=15, alphabet=hexdigits, prefix="session-")
    total = models.DecimalField(decimal_places=2, max_digits=2)
    user_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    updated_at = timezone.now()
    created_at = models.DateTimeField(timezone.now())

    class Meta:
        verbose_name = "Shopping Session"
        verbose_name_plural = "Shopping Sessions"

    def __repr__(self):
        return self.user_id