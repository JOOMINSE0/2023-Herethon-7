from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=32)
    userId = models.CharField(max_length=32)
    userPwd = models.CharField(max_length=32)
    userRrn1 = models.CharField(max_length=6, null=True)
    userRrn2 = models.CharField(max_length=1, null=True)
    userLink = models.CharField(max_length=2000)

    CHOICE_OPTIONS1 = (
        ('option1', '계획형'),
        ('option2', '즉흥형'),
    )
    CHOICE_OPTIONS2 = (
        ('option3', '바쁘게 움직이는 여행'),
        ('option4', '오직 휴식을 위한 여행'),
    )
    CHOICE_OPTIONS3 = (
        ('option5', '사진 찍는 거 좋아요'),
        ('option6', '사진 찍는 거 싫어요'),
    )
    CHOICE_OPTIONS4 = (
        ('option7', '번화가'),
        ('option8', '자연, 시골'),
    )
    userType1 = models.CharField(max_length=15, choices=CHOICE_OPTIONS1, default='option1')
    userType2 = models.CharField(max_length=15, choices=CHOICE_OPTIONS2, default='option3')
    userType3 = models.CharField(max_length=15, choices=CHOICE_OPTIONS3, default='option5')
    userType4 = models.CharField(max_length=15, choices=CHOICE_OPTIONS4, default='option7')
    
    image = models.ImageField(upload_to='images/', null=True, default='images/default_image.png')

    class Meta:
        db_table = 'user'
        verbose_name = 'Model_user'
        verbose_name_plural = 'Model_user'

    def __str__(self):
        return self.userName
    
class TempUser(models.Model):
    userName = models.CharField(max_length=32)
    userId = models.CharField(max_length=32)
    userPwd = models.CharField(max_length=32)
    userRrn1 = models.CharField(max_length=6, null=True)
    userRrn2 = models.CharField(max_length=1, null=True)
    userLink = models.CharField(max_length=2000)
    
    class Meta:
        db_table = 'tempUser'
        verbose_name = 'Model_tempUser'
        verbose_name_plural = 'Model_tempUser'

    def __str__(self):
        return self.userName
