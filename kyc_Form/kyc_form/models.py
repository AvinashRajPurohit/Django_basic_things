from PIL import Image
from django.db import models


# Create your models here.
class Details(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=300)
    phone_no = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    dob = models.DateField(max_length=20)
    pan_no = models.IntegerField()
    pin_code = models.IntegerField()
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    adhaar_img = models.ImageField(upload_to='adhaar', blank=True, null=True)
    pan_img = models.ImageField(upload_to='pan', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} with  Pan No.: {self.pan_no}'

    def save(self):
        super().save()
        img = Image.open(self.adhaar_img.path)
        img1 = Image.open(self.pan_img.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img1.thumbnail(output_size)
            img.save(self.adhaar_img.path)
            img1.save(self.pan_img.path)

    # def save(self):
    #     super().save()
    #     img = Image.open(self.pan_img.path)
    #
    #     if img.height > 300 and img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.pan_img.path)
