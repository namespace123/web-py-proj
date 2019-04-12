import web
import pymysql

# 定义模板文件夹
render = web.template.render('templates')

urls = (
    '/index', 'index',
    '/article', 'article',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello',
)
app = web.application(urls, globals())

class index:
    def GET(self):
        # 相对路径
        # return web.seeother('/article')
        # 绝对路径
        return web.seeother('http://www.baidu.com')

class blog:
    def POST(self):
        return web.input()

    def GET(self):
        return web.ctx.env

class hello:
    def GET(self, name):
        # 和 open.read 类似，好处是可以动态改变内容
        return render.hello2(name)

class article:
    def GET(self):
        conn = pymysql.connect(host='localhost', user='root', password='888',
                               db='awesome', charset='gbk', port=3306,
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        cur.execute("select * from blogs");
        r = cur.fetchall()
        cur.close()
        conn.close()
        print(r)
        return render.article(r)

if __name__ == "__main__":
    app.run()
