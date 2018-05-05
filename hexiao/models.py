from django.db import models
from django.contrib import admin


# 界面管理模型类
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'h_code', 'create_time', 'h_description', 'code_status', 'is_delete']
    search_fields = ['code']
    list_per_page = 15


# 核销码存储表
class HXCodeInfo(models.Model):
    # 核销码
    code = models.CharField(max_length=30,unique=True)
    # 核销码创建时间，自动默认填写创建时的时间
    createTime = models.DateField(auto_now=True)
    # 核销码的使用状态Flase为未使用，True为已使用
    codeStatus = models.BooleanField(default=False)
    # 核销码的描述信息
    description = models.CharField(max_length=100)
    # 核销码逻辑删除字段
    isDelete = models.BooleanField(default=False)

    # 管理界面的逻辑显示字段
    def code_status(self):
        if self.codeStatus:
            return '已核销'
        else:
            return '未核销'

    def is_delete(self):
        if self.isDelete:
            return '已删除'
        else:
            return '未删除'

    def create_time(self):
        return self.createTime

    def h_code(self):
        return self.code

    def h_description(self):
        return self.description

    code_status.short_description = '使用状态'
    is_delete.short_description = '逻辑删除'
    create_time.short_description = '创建时间'
    h_code.short_description = '核销码'
    h_description.short_description = '核销码详情'


# 向amin注册管理的模型表
admin.site.register(HXCodeInfo, QuestionAdmin)
