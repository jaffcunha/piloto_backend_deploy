from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_save

# Importacao para utilizar o custom lookup
from django.db.models import Lookup

# Avisando o Django sobre a implementacao do custom lookup
from django.db.models.fields import Field

# Importacao para utilizar a transformacao
from django.db.models import Transform

# Avisando o Django sobre a implementacao da transformacao
from django.db.models import IntegerField

# Create your models here.

class Pessoa(models.Model):
    nome_pessoa = models.CharField("Nome completo", max_length = 64)
    idade = models.IntegerField("Idade", max_length = 16)
    genero = models.CharField("Genero", max_length = 64)
    cpf = models.CharField("CPF", max_length = 64)
    empresa = models.CharField("Empresa", max_length = 64)
    cargo = models.CharField("Cargo ocupado", max_length = 64)


# Codigo da implementacao de um custom lookup exatamente como esta documentado para maior didatica

class Funcao(Lookup):
    lookup_name = 'func'

    def as_sql(self, qn, connection):
        lhs, lhs_params = self.process_lhs(qn, connection)
        rhs, rhs_params = self.process_rhs(qn, connection)
        params = lhs_params + rhs_params
        print params
        return '%s <> %s' % (lhs, rhs), params

# Avisando o Django sobre a implementacao do custom lookup
Field.register_lookup(Funcao)

# Codigo da implementacao de uma transformacao
# foram feitas algumas alteracoes da documentacao
# para se adequar ao template

class IdadeMenor(Transform):
    lookup_name = 'idmenor'

    def as_sql(self, qn, connection):
        lhs, params = qn.compile(self.lhs)
        return "ABS(%s)" % lhs, params

# Avisando o Django sobre a implementacao da transformacao
IntegerField.register_lookup(IdadeMenor)
