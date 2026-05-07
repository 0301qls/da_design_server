from configparser import SafeConfigParser
import os

def get_config(filepath):
    """Get config parser.

    :param filepath: a config filepath to read.
    :type filepath: str
    :return: a parser (Use it like a "dictionary")
    :rtype: configparser.SafeConfigParser
    """
    # os.environ을 전달하여 시스템 환경변수를 parser가 인식하게 합니다.
    parser = SafeConfigParser(os.environ)
    ret = parser.read(filepath)
    
    if not ret:
        print('get_config(): Failed to parser.read()')
        return False
        
    return parser
