from django.db import models

# Create your models here.




class Product(models.Model):
    SELECTION = [['野菜', '野菜'], ['肉類', '肉類'], ['フルーツ', 'フルーツ'], ['調味料', '調味料'], ['その他', 'その他']]
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    stock = models.IntegerField()
    cost = models.IntegerField()
    classification = models.CharField('分類', max_length=10, choices=SELECTION, default='その他')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Branch_one(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    stock = models.IntegerField()
    cost = models.IntegerField()
    classification = models.CharField('分類', max_length=10, default='その他')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
    
class Branch_two(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    stock = models.IntegerField()
    cost = models.IntegerField()
    classification = models.CharField('分類', max_length=10, default='その他')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class Branch_three(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    stock = models.IntegerField()
    cost = models.IntegerField()
    classification = models.CharField('分類', max_length=10, default='その他')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class Central_product(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    stock = models.IntegerField()
    cost = models.IntegerField()
    classification = models.CharField('分類', max_length=10, default='その他')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name