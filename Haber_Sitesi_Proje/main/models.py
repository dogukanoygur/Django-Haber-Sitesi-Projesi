from django.db import models
# Admin tarafında haberin editlenmesi 'ckeditor' tarafından sağlanıyor.
from ckeditor.fields import RichTextField
class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Kategoriler'

    def __str__(self):
        return self.title

# Haber Model
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=RichTextField()
    add_time=models.DateTimeField(verbose_name='Yayımlanma Tarihi')

    class Meta:
        verbose_name_plural='Haberler'
        # Paylaşılan haberin öne çıkması "ordering=['-add_time']"
        ordering=["-add_time"]
    def __str__(self):
        return self.title


# Yorumlar
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment
