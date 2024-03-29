# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지 분할 된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 파이썬은 __init__.py 먼저 확인하고 그 안에 있는 모듈로 허가를 내줌 -- 버그가 발생한 것을 빨리 허가를 안내주면 됨

# 예제 1                         # 파일명을 쭈루룩
import sub.sub1.module1         # 같은 경로 내에 있으면 바로 사용 가능
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()


# 예제 2
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()


# 예제 3
from sub.sub1 import *

module1.mod1_test1()
module1.mod1_test2()
