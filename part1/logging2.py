import logging

handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s = %s(name)s - %(levelname)-8s -%(message)s')

handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.debug('이 메시지는 개발자만 이해해요.')
logger.info('생각대로 동작 중')
logger.warning('곧 문제가 생길 가능성이 높음')
logger.error('문제가 생겼어요')
logger.critical('시스템이 다운됩니다')
