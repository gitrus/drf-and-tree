# Generated by Django 3.0.4 on 2020-03-26 17:18

from django.db import migrations


def fill_tree_sample_values(apps, schema_editor):
    Tree = apps.get_model("tree", "Tree")

    db_alias = schema_editor.connection.alias
    Tree.objects.using(db_alias).bulk_create([
        Tree(tree_id=1, name="корень1", parent_id=None),
        Tree(tree_id=2, name="корень2", parent_id=None),
        Tree(tree_id=3, name="1-уровень1 1", parent_id=1),
        Tree(tree_id=4, name="1-уровень1 2", parent_id=1),
        Tree(tree_id=5, name="1-уровень1 3", parent_id=1),
        Tree(tree_id=6, name="1-уровень2 1.1", parent_id=3),
        Tree(tree_id=7, name="1-уровень2 1.2", parent_id=3),
        Tree(tree_id=8, name="1-уровень2 2.1", parent_id=4),
        Tree(tree_id=9, name="2-уровень1 1", parent_id=2),
        Tree(tree_id=10, name="2-уровень1 2", parent_id=2)
    ])


def remove_sample_values(apps, schema_editor):
    Tree = apps.get_model("tree", "Tree")

    db_alias = schema_editor.connection.alias
    Tree.objects.using(db_alias).filter(tree_id__in=list(range(1,10))).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_tree_sample_values, remove_sample_values),
    ]
