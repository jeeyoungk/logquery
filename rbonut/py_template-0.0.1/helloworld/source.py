import common
import logging
import rbonut
import sys
import time

logging.basicConfig(filename='source.log',level=logging.DEBUG)

class Source:
    def __init__(self):
        self.produce_counter = 0

    def initialize(self, ctx):
        logging.info("computation initialized.")
        ctx.set_timer(common.in_future(1000))

    def process_record(self, ctx, record):
        logging.info("Got something! do something here!")

    def process_timer(self, ctx, timer):
        self.produce_counter += 1
        logging.info("generating a record. %s", self.produce_counter)
        ctx.produce_record("jee-input", "key", "value")
        ctx.set_timer(common.in_future(1000))

    def metadata(self):
        return rbonut.Metadata(
                name="jee-source",
                istreams=[],
                ostreams=["jee-input"]
                )

rbonut.serve_computation(Source())
