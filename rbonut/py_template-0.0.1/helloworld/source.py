import common
import json
import logging
import random
import sys
import time
import uuid
try:
    import rbonut
except ImportError:
    rbonut = None

r = random.Random()
logging.basicConfig(filename='source.log',level=logging.DEBUG)

# randomly generate data.

def generate_data():
    SOURCES = ["hermione", "harry", "ron", "dumbledore", "voldemort"]
    return {
        "data"   : str(uuid.uuid4()),
        "source" : SOURCES[r.randrange(len(SOURCES))],
        "time"   : time.time()
    }

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
        for i in range(10):
            ctx.produce_record("jee-input", "log", json.dumps(generate_data()))
        ctx.set_timer(common.in_future(1000))

    def metadata(self):
        return rbonut.Metadata(
                name="jee-source",
                istreams=[],
                ostreams=["jee-input", "jee-query"]
                )

# rbonut.serve_computation(Source())
# testing logic
source = Source()
print(generate_data())
