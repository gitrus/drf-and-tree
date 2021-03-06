from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Tree
from .serializer import TreeSerializer


@csrf_exempt
def tree_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    print(type(request))
    if request.method == 'GET':
        roots_trees = Tree.objects.filter(parent_id__isnull=True)

        serializer = TreeSerializer(roots_trees, many=True)

        return JsonResponse(
            {"result": serializer.data},
            safe=True,
        )

    else:
        raise NotImplementedError()
