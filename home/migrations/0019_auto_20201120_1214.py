# Generated by Django 3.1.3 on 2020-11-20 12:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20201120_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='product',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('carousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('product', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))]))]),
        ),
    ]