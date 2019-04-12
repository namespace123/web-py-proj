import web

urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class index:
    def GET(self):
        return web.input()

class blog:
    def POST(self):
        return web.input()

    def GET(self):
        return web.ctx.env

class hello:
    def GET(self, name):
        return open(r'static/hello.html').read()

if __name__ == "__main__":
    app.run()
