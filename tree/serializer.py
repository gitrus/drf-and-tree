from django.db import connection
from rest_framework import serializers
from .models import Tree

import typing as t

class TreeIsNotMutable(Exception):
    """Exception for abstrac method"""


class TreeSerializer(serializers.Serializer):
    def _build_cte(self, root_id):
        sql = f'''
            WITH RECURSIVE full_tree as (
                SELECT t1.id, t1.name, t1.parent_id
                FROM tree as t1
                    WHERE id = {root_id}
                UNION ALL
                SELECT t2.id, t2.name, t2.parent_id
                FROM tree as t2
                JOIN full_tree ON full_tree.id = t2.parent_id
            )
            SELECT * FROM full_tree;
        '''

        return sql

    def build_parent_based_tree(self, root: Tree, selected_tree: t.List[t.Tuple[int, str,int]]):
        result = {
            "id": root.id,
            "parent_Id": root.name,
            "name": root.parent,
            "childs": []
        }
        return result

    def to_representation(self, instance):
        if instance is None:
            return None

        cte = self._build_cte(instance.id)
        with connection.cursor() as cursor:
            cursor.execute(cte)
            tree = cursor.fetchall()

            return self.build_parent_based_tree(instance, tree)

    def update(self, instance, validated_data):
        raise TreeIsNotMutable()

    def create(self, validated_data):
        raise TreeIsNotMutable()

