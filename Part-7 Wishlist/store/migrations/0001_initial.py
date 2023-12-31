# Generated by Django 4.2.4 on 2023-08-23 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mptt2", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mptt_lft",
                    models.PositiveIntegerField(
                        editable=False,
                        help_text="The left value of the node",
                        verbose_name="left",
                    ),
                ),
                (
                    "mptt_rgt",
                    models.PositiveIntegerField(
                        editable=False,
                        help_text="The right value of the node",
                        verbose_name="right",
                    ),
                ),
                (
                    "mptt_depth",
                    models.PositiveIntegerField(
                        editable=False,
                        help_text="The hierarchy level of this node inside the tree",
                        verbose_name="depth",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Required and unique",
                        max_length=255,
                        unique=True,
                        verbose_name="Category Name",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255, unique=True, verbose_name="Category safe URL"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "mptt_parent",
                    models.ForeignKey(
                        editable=False,
                        help_text="The parent of this node",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chilren",
                        related_query_name="child",
                        to="store.category",
                        verbose_name="parent",
                    ),
                ),
                (
                    "mptt_tree",
                    models.ForeignKey(
                        editable=False,
                        help_text="The unique tree, where this node is part of",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_nodes",
                        related_query_name="%(app_label)s_%(class)s_node",
                        to="mptt2.tree",
                        verbose_name="tree",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Required", max_length=255, verbose_name="title"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Not Required", verbose_name="description"
                    ),
                ),
                ("slug", models.SlugField(max_length=255)),
                (
                    "regular_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="Maximum 999.99",
                        max_digits=5,
                        verbose_name="Regular price",
                    ),
                ),
                (
                    "discount_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99."
                            }
                        },
                        help_text="Maximum 999.99",
                        max_digits=5,
                        verbose_name="Discount price",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Change product visibility",
                        verbose_name="Product visibility",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="store.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="ProductSpecification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Required", max_length=255, verbose_name="Name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification",
                "verbose_name_plural": "Product Specifications",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        unique=True,
                        verbose_name="Product Name",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Product Type",
                "verbose_name_plural": "Product Types",
            },
        ),
        migrations.CreateModel(
            name="ProductSpecificationValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        help_text="Product specification value (maximum of 255 words",
                        max_length=255,
                        verbose_name="value",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "specification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="store.productspecification",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification Value",
                "verbose_name_plural": "Product Specification Values",
            },
        ),
        migrations.AddField(
            model_name="productspecification",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="store.producttype"
            ),
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="images/default.png",
                        help_text="Upload a product image",
                        upload_to="images/",
                        verbose_name="image",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        help_text="Please add alternative text",
                        max_length=255,
                        null=True,
                        verbose_name="Alternative text",
                    ),
                ),
                ("is_feature", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_image",
                        to="store.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="store.producttype"
            ),
        ),
    ]
