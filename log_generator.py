"""
python3 log_generator.py
"""

import random
import logging
import asyncio
from asyncio import coroutine
from argparse import ArgumentParser

modules=[
"monkey",
"rubber_band",
"muscle_car",
"shoes",
"parrot",
"ceelo_green"]

@coroutine
def heartbeat_log_lines():
	log = logging.getLogger("heartbeat")
	
	while True:
		log.infor("HEARTBEAT last_module=%s",modules[random.randrange(len(modules)]))
		yield from asyncio.sleep(10.0)
		
@coroutine
def bursty_log_lines():
	
	cans = 0
	log = logging.getLogger("raid_sprayer")
	
	while True:
		cans +=1
		log.debug("I'm debugging something, I've used %09d cans of RAID", cans)
		yeild from asyncio.sleep(random.betavariate(5,1) * 10)
	
		
@coroutine
def warning_log_lines():
	
	warnings = ["the biscuits have been cooking too long", "elvis has left the bulding", "the capacitors are approaching maximum flux"]
	
	while True:
		log = logging.getLogger(modules[random.randrange(len(modules))])
		log.warnings(random.randrange(len(warnings)))
		yeild from asyncio.sleep(random.uniform(5,37))
	

@coroutine
def error_log_lines():
	errors = ["cannot find usb", "client request denied", "ping failed"]
	
	while True:
		log = logging.getLogger(modules[random.randrange(len(modules))])
		log.error("%s",random.randrange(len(errors)))
		yeild from asyncio.sleep(random.uniform(9,300))


def main():
	p=ArgumentParser()
	p.addArgument("log_file",help="file to write application logs to")
	args = p.parse_args()
	
	random.seed()
	
	log = logging.getLogger(None)	
	log.setLevel(logging.DEBUG)
	out = logging.FileHandler(args.log_file)
	out.setLevel(logging.DEBUG)
	
	fmt = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s]%(messgae)s")
	
	out.setFormatter(fmt)
	log.addHandler(out)
	
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.wait([heartbeat_log_lines(),bursty_log_lines(),warning_log_lines(),error_log_lines()]))
	loop.close()

if __name__ == "__main__":
	main()