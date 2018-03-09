# get、post、g对象、before_request钩子函数、context_request钩子函数

## URL详解

1. URL是Uniform Resource Locator的简写，统一资源定位符。
2. 一个URL由以下几部分组成：

``` url
scheme://host:port/path/?query-string=xxx#anchor
```

* scheme:代表的是访问的协议，一般为HTTP或者https以及ftp等。
* host：主机名，域名，比如www.baidu.com。
* path：查找路径。比如www.jianshu.com/treding/now，后面的trending/now就是path。
* query-string：查询字符串，比如www.baidu.com/s?wd=python，后面的wd=python就是查询字符串。
* anchor:锚点，后台一般不用管，前段用来做页面定位的。

## get请求和post请求：

1. get请求：
* 使用场景：如果只对服务器获取数据，并没有对服务器产生任何影响，那么这时候使用get请求。
* 传参：get请求传参是放在URL中，并且通过‘？’的形式来指定key和value的。

2. post请求：
* 使用场景：如果要对服务器产生影响，那么就使用post请求。
* 传参：post请求传参不是放在URL中，是通过‘from data’的形式发送给服务器的。

## 01、get和post 请求获取参数：

1. get 请求是通过‘flask.request.args’来获取。
2. post 请求是通过‘flask.request.form’来获取。
3. post 请求在模版中要注意几点：

* input标签中，要写name来标识这个value和key,方便后台获取。
* 在写form表单的时候，要指定‘method='post'’,并且要指定‘action='/login/'’。

## 02保存全局变量的g属性

g:global

1. g对象是专门用来保存用户的数据的。
2. g对象在一次请求中的所有的代码的地方，都是可以使用的。

## 03钩子函数：

1. before_request:

* 在请求之前执行的。
* 是在试图函数执行之前执行的。
* 这个函数只是一个装饰器，他可以把需要设置为钩子函数的代码放到视图函数执行之前来执行

2. context_processor:

* 上下文处理器应该返回一个字典，字典中的‘KEY’会被模版中当成变量来渲染。
* 上下文处理器中返回的字典，在所有页面中都是可用的。
* 被这个装饰器修饰的钩子函数，必须要返回一个字典，即使为空也要返回。