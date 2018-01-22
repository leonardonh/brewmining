from django.contrib import admin

from .models import Batelada, Medida

admin.site.register(Batelada)
admin.site.register(Medida)

from .models import Batelada2, Medida2

admin.site.register(Batelada2, name='Batelada')
admin.site.register(Medida2, name='Batelada')
