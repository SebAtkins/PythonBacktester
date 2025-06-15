from engine import Engine
from customStrategy import SimpleStrategy
from datetime import *

eng: Engine = Engine()
eng.addStrategy(SimpleStrategy())
eng.setTimes(date(2020, 1, 1), date(2020, 12, 31), timedelta(days=1))
eng.run()

# TODO: Fetch x days worth of data at a time
