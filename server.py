import json
import time
import main
from tornado import gen
import tornado.ioloop
import tornado.web


class DataHandler(tornado.web.RequestHandler):

    def task(self, callback):
        la = float(self.get_argument('la'))
        mu = float(self.get_argument('mu'))
        nu = float(self.get_argument('nu'))
        N = int(self.get_argument('N'))
        Nk = int(self.get_argument('Nk'))
        Np = int(self.get_argument('Np'))
        model_type = self.get_argument('dir')

        p, N_avg, solve_time = main.perform(la, mu, nu, N, Nk, Np, model_type)
        p_str = main.print_p(p)
        resp_dict = {
            'p': p_str,
            'N_avg': N_avg,
            'solve_time': solve_time
        }
        callback(resp_dict)

    @gen.coroutine
    def get(self):
        response = yield gen.Task(self.task)

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(response))
        self.finish()

application = tornado.web.Application([
    (r"/data", DataHandler),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': './static'}),
])


if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
