from django.core.management.base import BaseCommand
from django.utils.text import slugify
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
                'slug': 'wireless-earbuds-pro'
            },
            {
                'name': 'Smartphone X',
                'price': 899.99,
                'description': 'Latest smartphone with advanced camera and performance.',
                'slug': 'smartphone-x'
            },
            {
                'name': 'Ergonomic Keyboard',
                'price': 89.99,
                'description': 'Comfortable keyboard designed for long typing sessions.',
                'slug': 'ergonomic-keyboard'
            },
            {
                'name': '4K UHD Monitor',
                'price': 349.99,
                'description': '27-inch 4K monitor with HDR support.',
                'slug': '4k-uhd-monitor'
            },
            {
                'name': 'Wireless Charging Pad',
                'price': 29.99,
                'description': 'Fast wireless charger for all Qi-enabled devices.',
                'slug': 'wireless-charging-pad'
            }
        ]

        # Clear existing products
        Product.objects.all().delete()

        # Create new products with slugs
        for product_data in products:
            # Create slug from name if not provided
            if 'slug' not in product_data:
                product_data['slug'] = slugify(product_data['name'])
            
            product = Product.objects.create(
                name=product_data['name'],
                price=product_data['price'],
                description=product_data['description'],
                slug=product_data['slug']
            )
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name} with slug: {product.slug}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded product data!'))