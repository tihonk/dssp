from django.db import models


class Dssp(models.Model):
    protein_name = models.CharField('PDB name', max_length=200)
    dssp_content = models.TextField('full DSSP context')
    count_date = models.DateTimeField('count date')


class DsspCalcResult(models.Model):
    pass
