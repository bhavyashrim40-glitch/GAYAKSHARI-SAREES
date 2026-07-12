from django.db import models

# ಗ್ರಾಹಕರ ಆರ್ಡರ್ ವಿವರಗಳ ಟೇಬಲ್ (ಇದು ಹಾಗೇ ಇರಲಿ)
class SareeOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    shipping_address = models.TextField()
    saree_name = models.CharField(max_length=100)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.saree_name}"


# ನವೀಕರಿಸಿದ ಪ್ರೊಡಕ್ಟ್ ಮಾಡೆಲ್ (ಇಲ್ಲಿ ಹಳೆಯ ಪ್ರೊಡಕ್ಟ್ ಕೋಡ್ ಬದಲಿಗೆ ೪ ಫೋಟೋಗಳ ಹೊಸ ಕೋಡ್ ಹಾಕಲಾಗಿದೆ)
class Product(models.Model):
    name = models.CharField(max_length=255)                  # ಸೀರೆಯ ಹೆಸರು
    price = models.IntegerField()                             # ಸೀರೆಯ ಬೆಲೆ
    
    # ಒಂದೇ ಸೀರೆಯ ೪ ವಿಭಿನ್ನ ಫೋಟೋಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಲು ಫೀಲ್ಡ್‌ಗಳು
    image1 = models.ImageField(upload_to='products/')         # ಮುಖ್ಯ ಫೋಟೋ (ಕಡ್ಡಾಯ)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True) # ಐಚ್ಛಿಕ ಫೋಟೋ ೨
    image3 = models.ImageField(upload_to='products/', blank=True, null=True) # ಐಚ್ಛಿಕ ಫೋಟೋ ೩
    image4 = models.ImageField(upload_to='products/', blank=True, null=True) # ಐಚ್ಛಿಕ ಫೋಟೋ ೪
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name