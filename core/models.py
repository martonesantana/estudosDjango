from django.db import models
from stdimage.models import StdImageField 
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now_add=True)
    active = models.BooleanField('Active', default=False)

    class Meta:
        abstract = True

class company(Base):
    cnpj = models.CharField('CNPJ',max_length=80, null=False, blank=False,unique=True)
    data_abertura = models.DateField('Data de Abertura',null=False, blank=False)
    razao_social = models.CharField('Razão Social',max_length=100,null=False, blank=False)
    nome_fantasia = models.CharField('Nome Fantasia',max_length=100,null=False, blank=False)
    logradouro = models.CharField('Logradouro',max_length=150,null=False, blank=False)
    numero = models.CharField('Número',max_length=20,null=False, blank=False)
    cep = models.CharField('CEP', max_length=10,null=False, blank=False)
    bairro = models.CharField('Bairro', max_length=20,null=False, blank=False)
    municipio = models.CharField('Municipio', max_length=50,null=False, blank=False)
    uf = models.CharField('UF', max_length = 2, null=False, blank=False)
    email = models.CharField('Email',max_length=30,null=False, blank=False, unique=True)
    telefone = models.CharField('Telefone',max_length=20,null=False, blank=False)
    logo = StdImageField('Logo', upload_to='medias/empresas/logo', variations={'thumb': (124,124)})
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nome_fantasia

    