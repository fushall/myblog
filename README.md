# myblog




##### 一键安装myblog所需要的各种库
```shell
pip install -r requirements.txt
```

##### 搭建环境
Python3.6.5 + Flask 1.0.2 + Centos7 + MariaDB  


##### 配置文件的修改

`myblog/configs/`目录下的即为配置文件，`configs`是一个python包（package）  
`__init__.py`的register_configs方法，自动包含了这个包下面的所有子py文件，  
也就是说，在里面新建个例如`flask_xxxx.py` 文件的时候，不用import了。  
再说一下每个py文件的结构，比如`flask_sqlalchemy.py`，里面有三个类，分别  
是`Defalut`、`Development`和`Production`，其中`Default`类名字可以任意，  
作用是为`Development`和`Production`提供了“共同不变的配置项”。  
对于`Development`，在debug模式下，会把这个类里面的内容当作配置，反之  
则是`Production`。register_configs的源代码如下：  
```python
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