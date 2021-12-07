from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re


@csrf_exempt
def dsspcalc(request):

    if request.method == 'POST':
        pdb_file_content = request.FILES['pdbFile'].read().decode('UTF-8')
        full_atom_coordinates = re.findall(r'ATOM(.*)\n', pdb_file_content)
        chain = request.POST['chain']
    return HttpResponse(pdb_file_content)
