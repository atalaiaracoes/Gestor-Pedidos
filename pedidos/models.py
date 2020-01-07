from django.db import models
from datetime import datetime


class Produto(models.Model):
    cd_produto = models.AutoField(primary_key=True, blank=False)
    ds_produto = models.CharField(max_length=200, null=False)
    ds_ean_dun = models.CharField(max_length=15, null=False)
    ds_und_medida = models.CharField(max_length=10, null=False)
    qt_embalagem = models.IntegerField()


class Comprador(models.Model):
    cd_comprador = models.AutoField(primary_key=True, blank=False)
    cd_cnpj = models.CharField(max_length=20, null=False, blank=False)
    cd_eancomprador = models.CharField(max_length=15, null=False, blank=False)
    nm_razaosocial = models.CharField(max_length=300, null=False, blank=False)


class Fornecedor(models.Model):
    cd_fornecedor = models.AutoField(primary_key=True, blank=False)
    cd_cnpj = models.CharField(max_length=20, null=False, blank=False)
    cd_eanfornecedor = models.CharField(max_length=15, null=False, blank=False)
    nm_razaosocial = models.CharField(max_length=300, null=False, blank=False)


class Pedido(models.Model):
    cd_order = models.AutoField(primary_key=True, blank=False)
    cd_pedido = models.CharField(max_length=20, null=False, blank=False)
    vl_pedido = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    ds_tipopedido = models.CharField(max_length=10, null=False, default='')
    ds_funcao = models.CharField(max_length=10, null=False, default='')
    qt_itens = models.IntegerField(null=False, blank=False)
    dt_emissao = models.DateField(default=datetime.now, blank=True)
    ds_condicaoentrega = models.CharField(max_length=10, null=False, default='')
    dt_entregainicio = models.DateField(default=datetime.now, blank=True)
    dt_entregafinal = models.DateField(default=datetime.now, blank=True)
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)


class ItensPedido(models.Model):
    cd_itempedido = models.IntegerField(null=False, blank=False)
    qt_itenspedido = models.IntegerField()
    vl_itempedido = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    vl_descontoitem = models.DecimalField(max_digits=8, decimal_places=2)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
