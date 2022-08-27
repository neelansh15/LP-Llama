from django.db import models


class Block(models.Model):
    date = models.DateField(unique=True)
    block_no = models.IntegerField()

    def __str__(self):
        return f"{self.date}: {self.block_no}"


class Exchange(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_lps = models.IntegerField()
    chain_ids = models.TextField()


class Lp:
    address = models.CharField(max_length=50, unique=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    token0 = models.CharField(max_length=50)
    token1 = models.CharField(max_length=50)
    chain_ids = models.TextField()
