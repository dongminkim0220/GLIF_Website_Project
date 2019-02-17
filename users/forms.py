from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Glifer, Applicant, Subject

from django.db import transaction

class GliferSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_glifer = True
        user.save()
        glifer = Glifer.objects.create(user=user)
        return user

class ApplicantSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_applicant = True
        user.save()
        applicant = Applicant.objects.create(user=user)
        return user


class GliferEditForm(forms.ModelForm):
    class Meta:
        model = Glifer
        fields = '__all__'
        exclude = ['user', 'is_authorized', 'priority', 'is_mentor']

        labels = {
            "name_kr" : "한글 성명",
            "name_en" : "영문 성명",
            "birthdate" : "생일 (YYYY-MM-DD)",
            "phonenumber": "전화번호",
            "nth": "기수",
            "work_at": "직장 혹은 인턴(재학생의 경우, 적지 않으셔도 무방합니다.)",
            "profile_img": "프로필 사진 업로드(업로드 하지 않을 경우, 기본 사진으로 설정됩니다.)",
            "self_intro": "자기소개(홈페이지 메인화면에 업로드 됩니다.)",
            "self_intro_add": "추가적인 사항을 적어주세요.(경력 등)",
            "career_cur_detail": "현재 근무하고 있는 곳을 적어주세요. 형식은 '회사명 부서 직급 (자격증)' 을 지켜주세요. (ex. 글리프증권 채권발행부 과장 (CFA))",
            "career_prev_1_detail": "과거 근무지, 혹은 인턴경험등을 적어주세요.(1)",
            "career_prev_2_detail": "과거 근무지, 혹은 인턴경험등을 적어주세요.(2)",
        }

        

class ApplicantEditForm(forms.ModelForm):
    havetaken_courses = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label = "수강한 과목"
    )

    willtake_courses = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label = "이번학기 수강 과목"
    )
    class Meta:
        model = Applicant
        fields = '__all__'
        exclude = ['user',]

        labels =  {
            "name_kr" : "한글 성명",
            "birthdate" : "생일 (YYYY-MM-DD)",
            "schyr": "학년",
            "stu_id": "학번",
            "phonenumber": "전화번호",
            "grad": "졸업 예정일 (YYYY-MM-DD)",
            "extra": "인턴경험, 학회, 동아리, 수상경력등의 사항을 적어주세요.",
            "testprep": "CPA, CFA, 국제FRM등 다른 특별한 시험을 준비하고 계십니까? 준비하고 계신다면 어떤 시험을 준비하고 계십니까?",
            "willyou": "최소 2학기 이상 연속으로 활동 하셔야 합니다. 그렇지 않으면 정회원 등록이 불가능합니다. 가능하십니까?",
            "millitary": "군 미필자인 경우, 군대는 언제 가실 계획이십니까?",
            "havetaken_courses": "수강한 과목",
            "willtake_courses": "이번학기 수강 과목",
            "glifmotive": "1. 글리프에 지원하게 된 동기를 서술해주세요. 학회에 들어온다면, 학회를 통해 얻고자 하는 것은 무엇인지 서술해 주세요. 분량제한은 없습니다.",
            "futureplan": "2. 졸업 후에 어떤 분야에서 일을 하고 싶은지, 혹은 어떤 특정 금융업에 관심이 있는지 설명해주세요. 분량제한은 없습니다.",
        }

    
