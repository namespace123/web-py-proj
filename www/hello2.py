import web

# url的三种匹配方式：精确匹配、模糊匹配、带组匹配
urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class index:
    def GET(self):
        return 'index method'


class blog:
    def GET(self):
        return 'blog method'


    def POST(self):
        return 'blog post method'


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'


if __name__ == "__main__":
    app.run()