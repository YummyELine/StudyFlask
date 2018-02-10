# 知识点：session、cookie、get、post、g对象、before_request钩子函数、context_request钩子函数。

---

## cookie：

1. cookie:在网站中，http请求是无状态的。也就是说即使第一次和服务器链接后并且登录成功后，第二次请求服务器依然不能指导当前请求是那一个用户。cookie的出现就是为了解决这个问题。第一次登陆后服务器返回一些数据(cookie)给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个了。cookie存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过4KB。因此使用cookie只能存储一些小量的数据。
2. 如果服务器返回了‘cookie’给浏览器，那么浏览器下次再请求相同的服务器的时候，就会自动把‘cookie’发送给服务器，这个过程，用户根本不需要管。
3. ‘cookie’是保存在浏览器中的，相对的是浏览器。

## session：

1. session:session和cookie的作用有点类似，都是为了存储用户相关的信息。不同的是，cookie是存储在本地浏览器，而session存储在服务器。存储在服务器的数据会更加安全，不容易被窃取。但存储在服务器也有一定弊端，就是会占用服务器资源，但现在服务器已经发展至今，一些session信息还是绰绰有余的。
2. 使用‘session’的好处：

* 敏感数据不是直接发送回给浏览器，而是发送回一个‘session_id’,服务器将‘session_id’和敏感数据做一个影射存储在‘session’（在服务器上面）中，更加安全。
* ‘session’可以设置过期时间，也从开一方面，保证了用户的账号安全。

## cookei 与 session

1. cookie和session结合使用：web开发发展至今，cookie和session的使用已经出现了一些非常成熟的方案。在如今的市场或者企业里，一般有两种存储方式：

* 存储在服务端：通过cookie存储一个session_id，然后具体的数据则是保存在session中，如果用户已经登录，则服务器会在cookie中保存一个session_id，下次再次请求的时候，会把该session_id携带上来，服务器根据session_id在session库中获取用户的session数据。就能知道该用户到底是谁，以及之前保存的一些状态信息。这种专业术语叫做server side session.
* 将session数据加密，然后存储在cookie中。这种专业术语叫做client side session。flask采用的就是这种方式，但是也可以替代乘其他形式

## flask中使用cookie和session

1. cookies：在Flask中操作cookies，是通过response对象操作，可以在response返回之前，通过response.set_cookie来设置，这个方法有以下几个参数需要注意：

* key:设置的cookie的key。
* value：key对应的value。
* max_age：改cookie的过期时间，如果不设置，则浏览器关闭后就会自动过期。
* expires：过期时间，应该是一个datetime类型。
* domain：该cookie在那个域名中有效，一般设置子域名，比如cms.example.com。
* path：该cookie在哪个路径下有效。

2. session：Flask中的session是通过from flask import session。然后添加值key和value进去即可。并且，flask中的session机制是将session信息加密，然后存储在cookie中。专业术语叫做client side session。

## 01 flask中的session工作机制：

1. flask中的session机制是：把敏感数据经过加密后放入‘session’中，然后再把‘session’存放到‘cookies’中，下次请求的时候，再从浏览器发送过来的‘cookie’中读取‘session’，然后在从‘session’中读取敏感数据，并进行解密，获取最终的用户数据。
2. flask的这种‘session’机制，可以节省服务器的开销，因为把所有的信息都存储到了客户端(浏览器)。
3. 安全是相对的，把‘session’放到‘cookie’中，经过加密，也是比较安全的。

## 02 操作session：

1. session的操作方式：
* 使用‘session’需要从‘flask’中导入‘session’，以后所有和‘session’相关的操作都是通过这个变量来的、
* 使用‘session’需要设置‘SECRET_KEY’，用来作为加密用的。并且这个‘SECRET_KEY’如果每次服务器启动后都变化的话，那么之前的‘session’就不能再通过当前这个‘SECRET_KEY’进行解密了。
* 操作‘session’的时候，跟操作字典是一样的。
* 添加‘session’：‘session['username']’。
* 删除：‘session.pop('username')’或者‘del session['username']’。
* 清除所有‘session’：‘session.clear()’。
* 获取‘session’：‘session.get('username')’。

2. 设置session的过期时间：

* 如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束。
* 如果设置了session的permanent属性为True,那么过期时间是31天。
* 可以通过给‘app.config’设置‘PERMANENT_SESSION_LIFETIME’来更改过期时间，这个值的数据类型是‘datetime.timedelay’类型。