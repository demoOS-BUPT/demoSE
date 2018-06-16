import ConfigParser

cp = ConfigParser.SafeConfigParser()
cp.read('Air.conf')

'''
global WIND
global ELEC_MONEY
global ELEC_TEMP
global MODE
global TEMP_FROM
global TEMP_TO
global TEMP_WIDTH
global DEFAULT_WIND
global DEFAULT_TEMP
global SYSTEM_TIME
global TEMP_CHANGE
'''

WIND = [0,float(cp.get('wind','low')), float(cp.get('wind','medium')), float(cp.get('wind', 'high'))]
ELEC_MONEY = float(cp.get('elec', 'money'))
ELEC_TEMP = float(cp.get('elec', 'temp'))
MODE = cp.get('air', 'mode')
TEMP_FROM = int(cp.get('air', 'tempFrom'))
TEMP_TO = int(cp.get('air', 'tempTo'))
TEMP_WIDTH = int(cp.get('air', 'tempWidth'))
TEMP_CHANGE = 1

DEFAULT_WIND = int(cp.get('air', 'defaultWind'))
DEFAULT_TEMP = float(cp.get('air', 'defaultTemp'))

SYSTEM_TIME = 60 * 1.0 / float(cp.get('system', 'systemTime'))

CURRENT_TEMP = 21

localTempChange = 0.2
localTempRange = 20
localInitTemp = 20