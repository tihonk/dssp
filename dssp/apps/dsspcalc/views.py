from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re


@csrf_exempt
def dsspcalc(request):
    if request.method == 'POST':
        pdb_file_content = request.FILES['pdbFile'].read().decode('UTF-8')
        for coordinate in re.findall(r'ATOM(.*)\n', pdb_file_content):
            full_atom_coordinates = addTripedAtomCoordinate(coordinate)
        chain = request.POST['chain']
    return HttpResponse(full_atom_coordinates[5])


def addTripedAtomCoordinate(coordinate, full_atom_coordinates=[]):
    full_atom_coordinates.append(coordinate.strip())
    return full_atom_coordinates
