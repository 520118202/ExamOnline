"""ExamOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from exam.views import GradeListViewSet, ExamListViewSet, PracticeListViewSet
from question.views import ChoiceListViewSet, FillListViewSet, JudgeListViewSet, ProgramListViewSet, CheckProgramApi
from record.views import ChoiceRecordListViewSet, FillRecordListViewSet, JudgeRecordListViewSet, \
    ProgramRecordListViewSet
from user.views import RegisterViewSet, StudentViewSet, UpdatePwdApi, ClazzListViewSet

router = DefaultRouter()

# 配置exams的url
router.register(r'exams', ExamListViewSet)
router.register(r'grades', GradeListViewSet)
router.register(r'choices', ChoiceListViewSet)
router.register(r'fills', FillListViewSet)
router.register(r'judges', JudgeListViewSet)
router.register(r'programs', ProgramListViewSet)
router.register(r'register', RegisterViewSet)
router.register(r'clazzs', ClazzListViewSet)
router.register(r'students', StudentViewSet)
router.register(r'practices', PracticeListViewSet)
router.register(r'records/choices', ChoiceRecordListViewSet)
router.register(r'records/fills', FillRecordListViewSet)
router.register(r'records/judges', JudgeRecordListViewSet)
router.register(r'records/programs', ProgramRecordListViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('docs/', include_docs_urls('Python在线考试系统')),
    path('api-auth/', include('rest_framework.urls')),
    path('jwt-auth/', obtain_jwt_token),
    path('check-program/', CheckProgramApi.as_view()),
    path('update-pwd/', UpdatePwdApi.as_view()),
    re_path('^', include(router.urls))
]
