from django.db import models


class Tree(models.Model):
    class Meta:
        db_table = 'tree'

    tree_id = models.AutoField(primary_key=True)

    parent = models.ForeignKey(
        db_column='parent_id',
        to='self',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Родитель',
    )
    name = models.CharField(max_length=255, verbose_name='Название')
