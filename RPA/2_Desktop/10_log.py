# import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s") #level이상의 로그를 모두 기록해준다.

# #debug < info < warning < error < critical
# logging.debug("아 이거 누가짠거야 ㅅㅂ 개같이도 짰네")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 좀 오래된거임. 옛날거라서 고장날수도 있음. 보안이 낮을수도 있고")
# logging.error("아 고장남 ㅋㅋㄹㅃㅃ")
# logging.critical("ㅈ됨 복구모태")

#터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
#시간 [로그레벨] 메시지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
#로그 레벨 설정
logger.setLevel(logging.DEBUG)

#스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

#File
filename = datetime.now().strftime("./RPA/2_Desktop/Files/mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트")