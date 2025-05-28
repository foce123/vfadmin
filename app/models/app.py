from tortoise import fields

from app.schemas.menus import MenuType

from .base import BaseModel, TimestampMixin
from .enums import MethodType


class App(BaseModel, TimestampMixin):
    appname = fields.CharField(max_length=30, description="应用名称", index=True)
    project = fields.CharField(max_length=10, description="项目名称", index=True)
    port = fields.IntField(default=8080, description="端口")
    path = fields.CharField(max_length=128, null=True, description="服务路径")
    desc = fields.CharField(max_length=500, null=True, description="服务描述")

    class Meta:
        table = "appname"