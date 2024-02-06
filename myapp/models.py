from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=200)

    def __str__(self)->str:
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self)->str:
        return self.name

class employee(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.CharField(max_length=12)
    bonus=models.CharField(max_length=12)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    
    phone=models.CharField(max_length=12)
    
    hire_date=models.DateField()


    def __str__(self)->str:
        return "%s %s %s"%(self.first_name,self.last_name,self.phone)
