import sys
import pdb

def test_logger():
    """Test logger."""
    from src import mylogger
    try:
        # 본인 경로로 설정
        m = mylogger.get_logger('test', '/home/u1010/da_design_server/log')
        m.debug('hi, debug')
    except Exception as e:
        print(e)
        return False
    return True

def test_config():
    """Test config."""
    from src import myconfig
    try:
        # 본인 경로로 설정
        m = myconfig.get_config('/home/u1010/da_design_server/share/test.config')
        print("key1= ", m['general'].get('key1'))
        print("key2= ", m['general'].get('key2'))
        print("key3= ", m['logger'].get('key3'))
    except Exception as e:
        print(e)
        return False
    return True

if __name__ == '__main__':
    target_step = []
    if len(sys.argv) >= 2:
        target_step = sys.argv[1].split(',')
    
    print('Test steps = ', target_step)

    # 인자가 없거나 'logger'가 포함되면 실행
    if not target_step or 'logger' in target_step:
        ret = test_logger()
        if not ret:
            raise Exception('Error when test_logger')
        print('Success - test_logger')

    # 인자가 없거나 'config'가 포함되면 실행
    if not target_step or 'config' in target_step:
        ret = test_config()
        if not ret:
            raise Exception('Error when test_config')
        print('Success - test_config')

    print('Test completed.')
