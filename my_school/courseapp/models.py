from django.db import models


class Course(models.Model):
    EASY = 'e'
    NORMAL = 'n'
    HARD = 'h'

    LEVELS = [
        (EASY, 'Для новичков'),
        (NORMAL, 'Не придумал для кого'),
        (HARD, 'Для старичков')
    ]

    name = models.CharField(
        max_length=512,
        blank=True,
        verbose_name='название',
        unique=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание'
    )
    img = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="фото",
    )
    price = models.IntegerField(
        null=False,
        verbose_name='цена',
        default=999
    )
    author = models.CharField(
        max_length=32,
        blank=True,
        verbose_name='автор'
    )
    level = models.CharField(
        max_length=1,
        choices=LEVELS,
        default=EASY
    )
    date = models.DateField(
        auto_created=True,
        verbose_name='дата создания'
    )

    def __str__(self):
        return self.name
