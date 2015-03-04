import common
import logging
import rbonut
import sys
import time

logging.basicConfig(filename='sink.log',level=logging.DEBUG)

class Sink:
    def __init__(self):
        pass

    def initialize(self, ctx):
        ctx.set_timer(common.in_future(1000))

    def process_record(self, ctx, record):
        logging.info("Got something! do something here!")

    def process_timer(self, ctx, timer):
        logging.info("ping %s", time.time())
        ctx.set_timer(common.in_future(1000))

    def metadata(self):
        return rbonut.Metadata(
                name='jee-sink',
                istreams=[("jee-input", "GROUP_BY"))],
                istreams=["jee-input"],
                ostreams=[]
                )
try:
    rbonut.serve_computation(Sink())
except Exception as e:
    logging.exception("Error while initializing.")
