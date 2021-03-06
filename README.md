# A simple template

### 1&#8195;setuptools是什么?
python的一个流行工具包,用于打包代码.

### 2&#8195;安装setuptools
pip install setuptools wheel

### 3&#8195;如何使用setuptools打包代码?
(1)以setuptools的标准目录结构组织工程  
(2)为每个包创建__init__.py文件.  
(3)创建并编写setup.py文件,作为打包脚本.  
(4)最后运行setup.py打包脚本.  

### (1)&#8195;标准目录结构是怎样的?  
以本工程为例
project/  
|-- package1/  
|&#8195;&#8195;|-- \__init__.py  
|&#8195;&#8195;|-- aaa.py  
|-- package2/  
|&#8195;&#8195;|-- \__init__.py  
|&#8195;&#8195;|-- bbb.py  
|-- README  
|-- LICENSE  
|-- setup.py  

### (2)&#8195;编写__init__.py
以本工程为例中一个叫say的包为例,
sayHello.py的源代码为
```python
def say_hello():
    print("hello")

def say_bye():
    print("bye")
```

\__init__.py的源代码为
```python
from __future__ import absolute_import
from .sayHello import *
```

### (3)&#8195;如何编写setup.py?
```python
import setuptools

setuptools.setup(
    # 包名称(该名称仅用于对外显示,比如pip list中看到的名字)
    name = "noob",
    version = "1.0",
    url="www.google.com",
    description="first package",
    
    # license           授权信息
    # long_description  程序详细描述
    # keywords          程序关键字列表

    # 作者信息
    author = "Jay",
    author_email = "jay@gmail.com",
    
    # maintainer        维护者
    # maintainer_email

    # 指出哪些文件夹有包要处理(通常为包含 __init__.py的文件夹)
    packages = ['play','say','tool'],
    
    # py_modules        需要打包的py源代码单文件列表
    # package_dir       指定哪些目录下的文件被映射到哪个源码包

    # 运行环境限制
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",

    # 当前模块依赖哪些包(若环境中没有,会从pypi下载安装)
    install_requires=['capstone>=4.0.1'],
    
    # 指定依赖包的下载地址
    #dependency_links = ['http://192.168.18.18/project/hhl/tool/zrong-0.2.1.tar.gz']

    # 项目依赖数据文件(数据文件必须放在项目目录内,且使用相对路径)
    # package_data={'myapp': ['data/*.yml'],}

    # 数据文件存在于项目外,参数为[(安装目录,源文件)]
    # data_files=[(‘mydata’, [‘data/conf.yml’])]
    
)
```

### (4)&#8195;执行setup.py,输出打包后的包文件
(1)sdist 表示源码包类型  
(2)bdist 表示二进制包类型  
(3)常见格式是egg\wheel\zip等  
(4)默认输出目录为xxxx\project目录\dist\  

任选一个包格式  
python setup.py sdist  
python setup.py bdist  
python setup.py bdist_egg  
python setup.py bdist_wheel  
python setup.py bdist_rpm  
python setup.py bdist_wininst  
python setup.py bdist_msi  

### 4&#8195;最后将包安装到其他电脑上
pip install xxxx\pack_name
