from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import Q
from tinymce.models import HTMLField

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


class ProductManager(models.Manager):
    def get_search(self, query):
        lookup = (
            Q(title__icontains=query)
            | Q(slug__icontains=query)
            | Q(short_description__icontains=query)
            | Q(content__icontains=query)
            | Q(category__name__icontains=query)
            | Q(category__slug__icontains=query)
            | Q(tags__name__icontains=query)
            | Q(tags__slug__icontains=query)
        )
        return (
            self.get_queryset()
            .filter(lookup)
            .order_by("-date_created")
            .all()
            .distinct()
        )


class Product(models.Model):
    STATUS = (("active", "فعال"), ("deactive", "غیرفعال"))
    title = models.CharField(max_length=100, verbose_name=_("عنوان محصول"))
    slug = models.SlugField(
        verbose_name=_("اسلاگ"),
        unique=True,
    )
    short_description = models.TextField(verbose_name=_("توضیحات مختصر"))
    content = HTMLField(verbose_name=_("توضیحات کامل"))
    keywords = models.TextField(
        verbose_name=_("Keywords"),
        help_text=_("مثال: چاقو، موبایل، ..."),
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="images/", verbose_name=_("عکس محصول"))
    price = models.BigIntegerField(default=0, verbose_name=_("قیمت(تومان)"))
    count = models.IntegerField(
        default=1,
        validators=[validators.MinValueValidator(0, "کمترین مقدار باید سفر باشد")],
        verbose_name=_("تعداد موجود در انبار"),
    )
    discount = models.FloatField(
        default=0,
        verbose_name=_("درصد تخفیف"),
        validators=[
            validators.MinValueValidator(0, "کمترین مقدار باید صفر باشد."),
            validators.MaxValueValidator(100, "بیشتر مقدار باید 100 باشد."),
        ],
    )
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

    objects = ProductManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def discount_price(self):
        if self.discount > 0:
            final_price = self.price - (self.price * (self.discount / 100))
            return final_price

    discount_price.short_description = "قیمت کل با تخفیف"

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


class Option(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("محصول"),
        related_name="options",
    )
    title = models.CharField(max_length=100, verbose_name=_("عنوان"))
    description = models.CharField(max_length=100, verbose_name=_("توضیحات کوتاه"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("آپشن")
        verbose_name_plural = _("آپشن ها")


class SetDiscount(models.Model):
    discount = models.FloatField(
        default=0,
        verbose_name=_("درصد تخفیف"),
        validators=[
            validators.MinValueValidator(0, "کمترین مقدار باید صفر باشد."),
            validators.MaxValueValidator(100, "بیشتر مقدار باید 100 باشد."),
        ],
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_("دسته بندی"),
        help_text=_("درصد تخفیف بر روی همه محصولات موجود در دسته بندی اصافه خواهد شد."),
    )

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = _("تخفیف")
        verbose_name_plural = _("تخفیفات بر اساس دسته بندی")

    def get_re_submit(self):
        if self.category.product_set.count() > 0:
            products = Product.objects.filter(category=self.category).all()
            for product in products:
                product.discount = self.discount
            super(Product, product).save(*args, **kwargs)
            super(SetDiscount, self).save(*args, **kwargs)

    def clean(self):
        if self.category.product_set.count() < 1:
            raise ValidationError({"category": "هیچ محصولی در این دسته بندی یافت نشد."})

    def save(self, *args, **kwargs):
        # do save discount in all products in category
        # if self.category.product_set.count() > 0:
        products = Product.objects.filter(category=self.category).all()
        for product in products:
            product.discount = self.discount
        super(Product, product).save(*args, **kwargs)
        super(SetDiscount, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        products = Product.objects.filter(category=self.category).all()
        for product in products:
            product.discount = 0
        super().delete(*args, **kwargs)
        super(Product, product).save(*args, **kwargs)