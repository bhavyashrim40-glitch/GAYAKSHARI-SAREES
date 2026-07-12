from django.contrib import admin
from .models import SareeOrder, Product  # ಇಲ್ಲಿ Product ಮಾಡೆಲ್ ಅನ್ನು ಸೇರಿಸಲಾಗಿದೆ

admin.site.register(SareeOrder)
admin.site.register(Product)            # ಅಡ್ಮಿನ್ ಪ್ಯಾನಲ್‌ನಲ್ಲಿ ಕಾಣಿಸಲು ಇದನ್ನು ರಿಜಿಸ್ಟರ್ ಮಾಡಲಾಗಿದೆ