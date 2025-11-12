from django.core.management.base import BaseCommand
from Products.models import Product

class Command(BaseCommand):
    help = 'Seeds the database with sample products'

    def handle(self, *args, **options):
        self.stdout.write('Seeding product data...')
        
        products = [
            {
                'name': 'Wireless Earbuds Pro',
                'price': 129.99,
                'description': 'High-quality wireless earbuds with noise cancellation and 24-hour battery life.',
                'active_product': True
            },
            {
                'name': 'Smartphone X',
                'price': 899.99,
                'description': 'Latest smartphone with 6.7" AMOLED display and triple camera system.',
                'active_product': True
            },
            {
                'name': 'Ergonomic Keyboard',
                'price': 79.99,
                'description': 'Mechanical keyboard with ergonomic design for comfortable typing.',
                'active_product': True
            },
            {
                'name': '4K UHD Monitor',
                'price': 349.99,
                'description': '27-inch 4K UHD monitor with HDR and 99% sRGB color gamut.',
                'active_product': True
            },
            {
                'name': 'Wireless Charging Pad',
                'price': 29.99,
                'description': 'Fast wireless charging pad compatible with all Qi-enabled devices.',
                'active_product': True
            }
        ]

        # Clear existing products
        Product.objects.all().delete()
        self.stdout.write('Deleted existing products...')

        # Create new products
        for product_data in products:
            Product.objects.create(**product_data)
            self.stdout.write(f"Created product: {product_data['name']}")

        self.stdout.write(
            self.style.SUCCESS('Successfully seeded product data!')
        )