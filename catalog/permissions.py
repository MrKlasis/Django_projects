from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


def create_moderator_group():
    moderator_group, created = Group.objects.get_or_create(name='Модераторы')

    content_type = ContentType.objects.get_for_model(Product)

    cancel_product_publication = Permission.objects.get(
        codename='cancel_product_publication',
        content_type=content_type,
    )

    change_product_description = Permission.objects.get(
        codename='change_product_description',
        content_type=content_type,
    )

    change_product_category = Permission.objects.get(
        codename='change_product_category',
        content_type=content_type,
    )

    moderator_group.permissions.add(
        cancel_product_publication,
        change_product_description,
        change_product_category,
    )