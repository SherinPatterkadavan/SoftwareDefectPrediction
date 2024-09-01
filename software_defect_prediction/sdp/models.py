from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class hr_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.IntegerField()
    post=models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    Email= models.CharField(max_length=100)

class tl_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    HR = models.ForeignKey(hr_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin= models.IntegerField()
    phone_no= models.BigIntegerField()
    email=models.CharField(max_length=100)

class tm_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    TL = models.ForeignKey(tl_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    phone_no = models.BigIntegerField()
    email = models.CharField(max_length=100)


class work_table(models.Model):
    HR= models.ForeignKey(hr_table, on_delete=models.CASCADE)
    TL= models.ForeignKey(tl_table, on_delete=models.CASCADE)
    work_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date=models.DateField()
    deadline=models.DateField()
    status=models.CharField(max_length=100)

class assign_table(models.Model):
    WORK=models.ForeignKey(work_table, on_delete=models.CASCADE)
    TM=models.ForeignKey(tm_table, on_delete=models.CASCADE)
    work_details=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=100)

class report_table(models.Model):
    ASSIGN= models.ForeignKey(assign_table, on_delete=models.CASCADE)
    report=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=100)

class result_table(models.Model):
    ASSIGN = models.ForeignKey(assign_table, on_delete=models.CASCADE)
    prediction_result=models.CharField(max_length=100)
    allocation=models.CharField(max_length=100)

class complaint_table(models.Model):
    TM= models.ForeignKey(tm_table, on_delete=models.CASCADE)
    complaint_details=models.CharField(max_length=100)
    date=models.DateField()
    replay=models.CharField(max_length=100)


class doubt_table(models.Model):
    TM= models.ForeignKey(tm_table, on_delete=models.CASCADE)
    doubt=models.CharField(max_length=100)
    date=models.DateField()
    replay=models.CharField(max_length=100)


class notification_table(models.Model):
    notifications=models.CharField(max_length=100)
    date=models.DateField()








