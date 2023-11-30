from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Смартфон'},
            {'name': 'Телевизо'},
            {'name': 'Холодильник'},
            {'name': 'Электрочайник'},
            {'name': 'Утюг'},
            {'name': 'Микроволновая печь'},
            {'name': 'Ноутбук'},
        ]
        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'Sony', 'price': '20000', 'category': Category.objects.get(name='Смартфон')},
            {'name': 'Sharp', 'price': '99999', 'category': Category.objects.get(name='Телевизо')},
            {'name': 'Полюс', 'price': '55000', 'category': Category.objects.get(name='Холодильник')},
            {'name': 'Vitek', 'price': '2500', 'category': Category.objects.get(name='Электрочайник')},
            {'name': 'LG', 'price': '34500', 'category': Category.objects.get(name='Смартфон')},
            {'name': 'ASUS', 'price': '32900', 'category': Category.objects.get(name='Ноутбук')},
            {'name': 'DELL', 'price': '45999', 'category': Category.objects.get(name='Ноутбук')},
        ]
        product_for_create = []
        for product in product_list:
            product_for_create.append(Product(**product))

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)
