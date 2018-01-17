# StudyFlask
自己学习Flask的一些笔记。

### 01 第一个flask程序讲解：
1. 第一次创建项目的时候，要添加flask的虚拟环境的时候，一定要选择到Python这个执行文件，比如如的flask的虚拟环境目录在/user/virtualenv/flask-env/bin/python.
2. 其他具体代码看.py文件

### 02 设置debug模式：
1. 在app.run()总传入一个关键字debug, app.run(debug = true),是设置当前项目为debug模式。
2. debug模式的两大功能：
* 当程序出现问题的时候，可以在页面中看到错误信息和出错的位置。
* 只要修改了项目中的'python'文件，程序会自动加载，不需要手动重新启动服务器。

### 03 使用配置文件
1. 新建一个'config.py'文件,文件里面写 DEBUG = True
2. 在主APP文件中导入这个文件，并且配置到‘APP’中，示例代码如下：
``` 
improt config
app.config.from_object(config)
```
3. 还有许多的其他参数，都是放在这个配置文件中，比如'SECRET_KEY'和'SQLALCHEMY'这些配置，都是在这个文件中。

### 04 URL传参数：
1. 参数的作用：可以在相同的URL，但是指定不同的参数，来加载不同的数据。
2.在Flask中如何使用参数：
```
@app.route('/article/<id>')
def article(id):
    return('您请求的参数是：{0}'.format(id))
```
* 参数需要放在两个尖括号中。
* 视图函数中需要放和URL总的参数同名的参数。

### 05 反转URL：
1. 什么叫做反转URL：从视图函数到URL的转换叫做反转URL
2. 反转URL的用处：
* 在页面重定向的时候，会使用URL反转。
* 在模板中，也会使用 URL反转。

### 06 页面跳转和重定向：
1. 用处：在用户访问一些需要登录的页面的时候，如果用户没有登录，那么可以让他重定向到登陆页面。
2. 代码实现：见PY文件， redirect()

### 07 Flask渲染Jinja2模板和传参：
1. 如何渲染模板：
* 模板放在'Templates'文件夹下。
* 从'flask'中导入'render_template'函数。
* 在视图函数中，使用'render_template'函数，渲染模板。注意：只需要填写模板的名字，不需要写'templates'这个文件夹的路径。
2. 模板传参：
* 如果只有一个或者少量参数，直接在'render_template'函数中添加关键字参数就可以了。
* 如果有多个参数的时候，那么可以先把所有的参数放在字典中，然后’render_template‘中，使用两个星号，把字典转换成关键参数传递进去，这样的代码更方便管理和使用。
3. 在模板中，如果要使用一个变量，语法是：‘{{params}}’
4. 访问模型中的属性或者字典，可用通过‘{{params.property}}'的形式，或者是使用‘{{params['age']}}'
