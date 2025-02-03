from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("عنوان"))
    slug = models.SlugField(verbose_name=_("اسلاگ"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("عنوان"))
    slug = models.SlugField(verbose_name=_("اسلاگ"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("تگ")
        verbose_name_plural = _("تگ ها")


class Product(models.Model):
    STATUS = (("active", "فعال"), ("deactive", "غیرفعال"))
    title = models.CharField(max_length=100, verbose_name=_("عنوان محصول"))
    slug = models.SlugField(verbose_name=_("اسلاگ"), blank=True, null=True)
    short_description = models.CharField(
        max_length=165, verbose_name=_("توضیحات مختصر")
    )
    content = models.TextField(verbose_name=_("توضیحات کامل"))
    image = models.ImageField(upload_to="images/", verbose_name=_("عکس محصول"))
    price = models.BigIntegerField(default=0, verbose_name=_("قیمت(تومان)"))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=_("دسته بندی")
    )
    tags = models.ManyToManyField(Tag, verbose_name=_("برچسب ها"), related_name="tags")
    status = models.CharField(
        max_length=50, choices=STATUS, default="active", verbose_name=_("وضعیت محصول")
    )
    date_created = models.DateTimeField(
        auto_now=False, auto_now_add=False, verbose_name=_("تاریخ ایجاد")
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # do save slug
        if self.slug == None:
            self.slug = self.title.replace(" ", "-")
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("محصول")
        verbose_name_plural = _("محصولات")


class Gallery(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("محصول"),
        related_name="galleries",
    )
    title = models.CharField(max_length=100, verbose_name=_("عنوان عکس"))
    image = models.ImageField(upload_to="products/images/", verbose_name=_("عکس"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("گالری")
        verbose_name_plural = _("گالری ها")
