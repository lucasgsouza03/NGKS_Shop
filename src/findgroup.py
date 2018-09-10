from SGU.models import Permissions

def get_groups(request):
    perm = Permissions.objects.filter(usuario_id__username=request.username)
    grupos = []
    for i in perm:
        i = str(i)
        grupos.append(i)
    return grupos