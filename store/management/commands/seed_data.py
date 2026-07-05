from django.core.management.base import BaseCommand
from store.models import Category, SubCategory

class Command(BaseCommand):
    help = 'Seed initial categories and subcategories'

    def handle(self, *args, **kwargs):
        # Safety Category
        safety, _ = Category.objects.get_or_create(
            name='Safety',
            defaults={'slug': 'safety', 'icon': 'fa-shield-alt', 'order': 1,
                       'description': 'Complete range of safety products and equipment'}
        )
        safety_subs = [
            'Sorbent Products', 'Gas Detector', 'Lockout-Tagout',
            'Safety Enclosure', 'Personal Protective Equipment',
            'Substation Safety Product', 'Area Marking',
            'Safety Signs', 'Safety Printers',
        ]
        for i, name in enumerate(safety_subs):
            SubCategory.objects.get_or_create(
                category=safety, name=name,
                defaults={'order': i}
            )

        # Electrical Category
        electrical, _ = Category.objects.get_or_create(
            name='Electrical',
            defaults={'slug': 'electrical', 'icon': 'fa-bolt', 'order': 2,
                       'description': 'Professional electrical engineering products'}
        )
        electrical_subs = [
            'Cable Tie', 'Cable Lug', 'Cable Terminal', 'Cable Gland',
            'Cable Sleeves', 'Bus Bar Insulators', 'Heat Shrink',
            'Cable Duct', 'Meters', 'Controllers', 'Protection',
            'Timers', 'Automation', 'Current Transformer Nylon Casing',
            'Identification', 'elmex Terminal Block',
        ]
        for i, name in enumerate(electrical_subs):
            SubCategory.objects.get_or_create(
                category=electrical, name=name,
                defaults={'order': i}
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
