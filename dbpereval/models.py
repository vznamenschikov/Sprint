from django.db import models


class dbPereval(models.Model):

    STATUS = [
        ('new', 'Новый'),
        ('pending', 'В обработке'),
        ('resolved', 'Завершен'),
        ('accepted', 'Принят'),
        ('rejected', 'Отменен'),
    ]

    date_added = models.DateTimeField(blank=True, null=True)
    raw_data = models.JSONField(blank=True)
    images = models.JSONField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='new')

    class Meta:
        db_table = 'pereval_added'
