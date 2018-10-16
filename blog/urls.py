from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]

#### ^post/(\d+)/$ #### 의미

# ^ : 문자열이 시작할 떄 : ^post/ : url이(오른쪽부터) post/로 시작(포함)합니다.
# $ : 문자열이 끝날 때 : $ : url 마지막이 /로 끝납니다.
# (?P<pk>\d+) : 이 정규표현식은 장고가 pk변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻
# \d : 숫자 : (\d+) : 숫자(한 개 이상)가 있습니다. 이 숫자로 조회하고 싶은 게시글을 찾을 수 있어요.
# : 바로 앞에 나오는 항목이 계속 나올 때
# () : 패턴의 부분을 저장할 때
# / : /뒤에 문자가 있습니다.
