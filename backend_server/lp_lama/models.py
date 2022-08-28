import logging

from django.db import models
import sys

logging.basicConfig(stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)


class Block(models.Model):
    date = models.DateField()
    chain_id = models.IntegerField()
    block_no = models.IntegerField()

    class Meta:
        unique_together = [['date', 'chain_id', 'block_no']]

    def __str__(self):
        return f"{self.date}: {self.block_no}"


class Exchange(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=50)
    reward_address = models.CharField(max_length=50)
    chain_id = models.IntegerField()

    class Meta:
        unique_together = [['address', 'chain_id']]

    def __str__(self):
        return f"{self.name}, {self.chain_id}"


class Lp(models.Model):
    address = models.CharField(max_length=50, db_index=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    pool_id = models.IntegerField()
    token0 = models.CharField(max_length=50)
    token1 = models.CharField(max_length=50)
    tvl = models.IntegerField()

    def __str__(self):
        return f"{self.token0}-{self.token1}: {self.exchange}"
