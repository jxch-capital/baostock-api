import core.breath as breath
import logging

logging.basicConfig(level=logging.DEBUG)
breath_map = breath.build_breath_1000d()

print(breath_map)
