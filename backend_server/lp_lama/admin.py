from django.contrib import admin
from lp_lama.models import *


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Lp)
class LpAdmin(admin.ModelAdmin):
    pass
