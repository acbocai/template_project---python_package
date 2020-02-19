import setuptools

setuptools.setup(
    # 包名称(该名称仅用于对外显示,比如pip list中看到的名字,与代码的引用无关)
    name = "noob",
    version = "1.0",
    url="www.google.com",
    description="first package",
    # license 授权信息
    # long_description 程序详细描述
    # keywords 程序关键字列表

    # 作者信息
    author = "Jay",
    author_email = "jay@gmail.com",
    # maintainer 维护者
    # maintainer_email

    # 指出哪些文件夹有包要处理(通常为包含 __init__.py的文件夹)
    packages = ['play','say','tool'],
    # py_modules 需要打包的py源代码单文件列表
    # package_dir  指定哪些目录下的文件被映射到哪个源码包

    # 运行环境限制
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",

    #
    platforms= "linux",

    # 当前模块依赖哪些包(若环境中没有,会从pypi下载安装)
    install_requires=['capstone>=4.0.1'],
    # 指定依赖包的下载地址
    #dependency_links = ['http://192.168.18.18/project/hhl/tool/zrong-0.2.1.tar.gz']

    # 项目依赖数据文件(数据文件必须放在项目目录内,且使用相对路径)
    # package_data={'myapp': ['data/*.yml'],}

    # 数据文件存在于项目外,参数为[(安装目录,源文件)]
    # data_files=[(‘mydata’, [‘data/conf.yml’])]

)