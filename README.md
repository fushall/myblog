# myblog
这是一个由Flask框架写的极简个人博客，新手友好，代码中的每一个变量名和方法，
都经过了上百次揣摩，非常适合刚入门的新手朋友，可以直接读代码，也可以改一改，
部署到自己的VPS上。预览地址如下：![blog.nmxxy.cn](http://blog.nmxxy.cn)



### 部署环境
Python3.6.5 + Flask 1.0.2 + Centos7 + MariaDB  


### 一键安装myblog所需要的各种库
```shell
pip install -r requirements.txt
```




### 配置文件的修改

`myblog/configs/`目录下的除了`__init__.py`，剩下所有的.py文件都是配置文件。
“configs”是一个python包（package），`__init__`.py的`register_configs`方法，
能够自动导入“configs包”下的所有子py模块（就是.py文件）。也就是说，在里面新建
例如“flask_xxxx.py” 文件的时候，不用手动import了。  

再说一下子py文件的内容，比如`flask_sqlalchemy.py`，里面有三个类，分别是
`Defalut`、`Development`和`Production`，其中`Default`的作用是把
`Development`和`Production`提供的“共同配置项”，集中起来了，不叫“Default”
也行，但是“Development” 和 “Production” 必须有，而且名字不能变。因为
在debug模式下，会把`Development`类里面的内容当作配置，反之
则是`Production`。`register_configs`的源代码如下：  
```python
# 取自configs/__init__.py

def register_configs(app):
    for module in iter_modules(__path__):
        if module.ispkg is False and module.name.startswith('_') is False:
            config_module = import_module(f'{__package__}.{module.name}')
			# 这个地方实现了根据debug模式读取相应配置
            if app.debug:
                config = config_module.Development
            else:
                config = config_module.Production
            app.config.from_object(config)

```