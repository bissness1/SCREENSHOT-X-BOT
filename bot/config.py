import os
from pathlib import Path

class Config:

    API_ID = int(os.environ.get('API_ID','6534707'))
    API_HASH = os.environ.get('API_HASH','4bcc61d959a9f403b2f20149cbbe627a')
    BOT_TOKEN = os.environ.get('BOT_TOKEN','5541380668:AAGH9yGr_4leFAgG35raDvAi1Q82ynMJGG0')
    SESSION_NAME = os.environ.get('SESSION_NAME', ':memory:')
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL','-1001843564893'))
    DATABASE_URL = os.environ.get('DATABASE_URL','mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority')
    AUTH_USERS = [int(i) for i in os.environ.get('AUTH_USERS', '').split(' ')]
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 3))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 6000))
    TRACK_CHANNEL = int(os.environ.get('TRACK_CHANNEL', False))
    SLOW_SPEED_DELAY = int(os.environ.get('SLOW_SPEED_DELAY', 5))
    HOST = os.environ.get('HOST', '')
    TIMEOUT = int(os.environ.get('TIMEOUT', 60 * 30))
    DEBUG = bool(os.environ.get('DEBUG'))
    IAM_HEADER = os.environ.get('IAM_HEADER', '')

    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]
    POSITIONS = ['Top Left', 'Top Center', 'Top Right', 'Center Left' , 'Centered', 'Center Right' , 'Bottom Left', 'Bottom Center', 'Bottom Right']
