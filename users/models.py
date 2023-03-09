from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, emp_name, ent_date, password=None):
        if not emp_name:
            raise ValueError('성함을 입력해 주세요 :)')

        user = self.model(
            emp_name=emp_name,
            ent_date = ent_date,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emp_name, ent_date, password=None):
        user = self.create_user(
            emp_name,
            ent_date,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'male'), # DB에는 "M", admin에는 "male"
        ('F', 'female'),
    )
    emp_name = models.CharField(max_length=10, verbose_name="직원 이름", null=True, unique=True)
    age = models.IntegerField(verbose_name="나이", null=True)
    ent_date = models.DateField(verbose_name="입사일")
    gender = models.CharField(verbose_name="성별",max_length=1, choices=GENDER_CHOICES, null=True)
    position = models.CharField(max_length=10, verbose_name="직군", null=True)
    address = models.CharField(max_length=100, null=True, verbose_name="주소", blank=True)
    rised_num = models.CharField(max_length=14, null=True, verbose_name="주민반호")
    zip_cde = models.CharField(max_length=7, null=True, verbose_name="우편 번호")
    retire_date = models.DateField(verbose_name="퇴사일", null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'emp_name'
    REQUIRED_FIELDS = ['ent_date']

    def __str__(self):
        return self.emp_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin