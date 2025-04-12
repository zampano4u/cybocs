import streamlit as st
import streamlit.components.v1 as components

# 참고문헌:
# Scahill, L., Riddle, M. A., McSwiggin-Hardin, M., Ort, S. I., King, R. A.,
# Goodman, W. K., Cicchetti, D. & Leckman, J. F. (1997). Children's Yale-Brown Obsessive Compulsive Scale: reliability and validity.
# Journal of the American Academy of Child & Adolescent Psychiatry, 36(6), 844-852.
#
# 이 프로그램은 업로드하신 CYBOCS 어린이판 자료()를 기반으로 제작되었습니다.


# 도입 증상 체크리스트용 한영 매핑 구조 (CYBOCS 어린이판 자료 반영)
cybocs_mapping = {
    "aggressive_obsessions": {
        "question_ko": "공격 관련 강박사고",
        "question_en": "AGGRESSIVE OBSESSIONS",
        "items": [
            {"ko": "자신에게 해를 입힐지도 모른다는 두려움", "en": "Fear might harm self"},
            {"ko": "타인에게 해를 입힐지도 모른다는 두려움", "en": "Fear might harm others"},
            {"ko": "폭력적이거나 끔찍한 이미지", "en": "Violent or horrific images"},
            {"ko": "욕설이나 모욕적인 말을 갑자기 내뱉을지도 모른다는 두려움", "en": "Fear of blurting out obscenities or insults"},
            {"ko": "다른 당혹스러운 행동을 할지도 모른다는 두려움", "en": "Fear of doing something else embarrassing"},
            {"ko": "원치 않는 충동(예: 가족 구성원을 찌를 것 같은 충동)을 실행할지도 모른다는 두려움", "en": "Fear will act on unwanted impulses (e.g., to stab a family member)"},
            {"ko": "물건을 훔칠지도 모른다는 두려움", "en": "Fear will steal things"},
            {"ko": "자신이 충분히 주의하지 않아 타인에게 해를 입힐지도 모른다는 두려움 (예: 뺑소니 사고)", "en": "Fear will harm others because of insufficient caution (e.g., hit/run accident)"},
            {"ko": "자신이 끔찍한 일을 일으킬지도 모른다는 두려움 (예: 화재, 절도, 홍수 등)", "en": "Fear will be responsible for something else terrible happening (e.g., fire, burglary, flood)"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "contamination_obsessions": {
        "question_ko": "오염 관련 강박사고",
        "question_en": "CONTAMINATION OBSESSIONS",
        "items": [
            {"ko": "체액이나 분비물(예: 소변, 대변, 침 등)에 대한 혐오감 또는 염려", "en": "Concerns or disgust with bodily waste or secretions (e.g., urine, feces, saliva)"},
            {"ko": "먼지나 세균에 대한 걱정", "en": "Concern with dirt or germs"},
            {"ko": "환경 오염물질(예: 석면, 방사능, 유독 폐기물 등)에 대한 과도한 걱정", "en": "Excessive concern with environmental contaminants (e.g., asbestos, radiation, toxic waste)"},
            {"ko": "가정용 물품(예: 세정제, 용제 등)에 대한 과도한 걱정", "en": "Excessive concern with household items (e.g., cleansers, solvents)"},
            {"ko": "동물(예: 곤충 등)에 대한 과도한 걱정", "en": "Excessive concern with animals (e.g., insects)"},
            {"ko": "끈적끈적한 물질이나 잔여물에 대한 불쾌감", "en": "Bothered by sticky substances or residues"},
            {"ko": "오염물질로 인해 병에 걸릴지도 모른다는 걱정", "en": "Concerned about getting ill because of contaminants"},
            {"ko": "오염물질로 인해 타인이 병에 걸릴지도 모른다는 걱정", "en": "Concerned about spreading contaminants to others (Aggressive)"},
            {"ko": "오염의 결과보다는 그 느낌에 대한 불쾌감", "en": "No concern with consequences of contamination other than the unpleasant feeling"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "sexual_obsessions": {
        "question_ko": "성적 강박사고",
        "question_en": "SEXUAL OBSESSIONS",
        "items": [
            {"ko": "금기되거나 일탈적인 성적 생각, 이미지 또는 충동", "en": "Forbidden or perverse sexual thoughts, images, or impulses"},
            {"ko": "아동 또는 근친상간 관련 내용", "en": "Content involves children or incest"},
            {"ko": "동성애 관련 내용", "en": "Content involves homosexuality"},
            {"ko": "타인을 대상으로 한 성적 행동 (공격적)", "en": "Sexual behavior toward others (Aggressive)"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "hoarding_saving_obsessions": {
        "question_ko": "저장/보존 강박사고",
        "question_en": "HOARDING/SAVING OBSESSIONS",
        "items": [
            {"ko": "저장/보존 강박사고 [취미나 금전적/정서적 가치와 구별]", 
             "en": "Hoarding/Saving obsessions [distinguish from hobbies and concern with objects of monetary or sentimental value]"}
        ]
    },
    "religious_obsessions": {
        "question_ko": "종교적 강박사고",
        "question_en": "RELIGIOUS OBSESSIONS",
        "items": [
            {"ko": "신성모독이나 불경에 대한 걱정", "en": "Concern with sacrilege or blasphemy"},
            {"ko": "옳고 그름, 도덕성에 대한 과도한 걱정", "en": "Excessive concern with right/wrong, morality"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "symmetry_exactness_obsession": {
        "question_ko": "대칭 또는 정확성에 관한 강박사고",
        "question_en": "OBSESSION WITH NEED FOR SYMMETRY OR EXACTNESS",
        "items": [
            {"ko": "마법적 사고 동반 (예: 물건 배치 불일치 시 사고 발생 우려)", 
             "en": "Accompanied by magical thinking (e.g., concern that an accident may occur unless things are properly arranged)"},
            {"ko": "마법적 사고 미동반", "en": "Not accompanied by magical thinking"}
        ]
    },
    "miscellaneous_obsessions": {
        "question_ko": "기타 강박사고",
        "question_en": "MISCELLANEOUS OBSESSIONS",
        "items": [
            {"ko": "알아야 하거나 기억해야 한다는 필요성", "en": "Need to know or remember"},
            {"ko": "특정 말을 해야 한다는 두려움", "en": "Fear of saying certain things"},
            {"ko": "정확한 표현을 하지 않으면 안 된다는 두려움", "en": "Fear of not saying just the right thing"},
            {"ko": "물건 분실에 대한 두려움", "en": "Fear of losing things"},
            {"ko": "침습적인(비폭력적) 이미지", "en": "Intrusive (non-violent) images"},
            {"ko": "무의미한 소리, 단어, 음악에 대한 침습적 경험", "en": "Intrusive nonsensical sounds, words or music"},
            {"ko": "특정 소리나 소음에 대한 불쾌감 *", "en": "Bothered by certain sounds/noises *"},
            {"ko": "행운/불운을 상징하는 숫자", "en": "Lucky/unlucky numbers"},
            {"ko": "특별한 의미의 색깔", "en": "Colors with special significance"},
            {"ko": "미신적 공포", "en": "Superstitious fears"}
        ]
    },
    "somatic_obsessions": {
        "question_ko": "신체 관련 강박사고",
        "question_en": "SOMATIC OBSESSIONS",
        "items": [
            {"ko": "질병이나 병에 대한 과도한 걱정 *", "en": "Excessive concern with illness or disease *"},
            {"ko": "신체 부위 또는 외모에 대한 과도한 걱정 (예: 신체이형장애) *", "en": "Excessive concern with body part or appearance (e.g., dysmorphophobia) *"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "cleaning_washing_compulsions": {
        "question_ko": "청결/세척 강박행동",
        "question_en": "CLEANING/WASHING COMPULSIONS",
        "items": [
            {"ko": "과도하거나 의례적인 손 씻기", "en": "Excessive or ritualized handwashing"},
            {"ko": "과도하거나 의례적인 샤워, 목욕, 양치, 미용, 또는 화장실 사용", "en": "Excessive or ritualized showering, bathing, toothbrushing, grooming, or toileting"},
            {"ko": "가정용 물품 또는 무생물 청소", "en": "Cleaning of household items or inanimate objects"},
            {"ko": "오염물질 접촉 방지 및 제거 행동", "en": "Other measures to prevent or remove contact with contaminants"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "checking_compulsions": {
        "question_ko": "확인 강박행동",
        "question_en": "CHECKING COMPULSIONS",
        "items": [
            {"ko": "자물쇠, 가스레인지, 가전제품 등 확인", "en": "Checking locks, stove, appliances, etc."},
            {"ko": "타인에게 해를 끼치지 않았는지 확인", "en": "Checking that did not/will not harm others"},
            {"ko": "자신에게 해를 끼치지 않았는지 확인", "en": "Checking that did not/will not harm self"},
            {"ko": "끔찍한 일이 발생하지 않았는지 확인", "en": "Checking that nothing terrible did/will happen"},
            {"ko": "실수하지 않았는지 확인", "en": "Checking that no mistake was made"},
            {"ko": "신체 관련 강박사고와 연관된 확인", "en": "Checking tied to somatic obsessions"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "repeating_rituals": {
        "question_ko": "반복 의례행동",
        "question_en": "REPEATING RITUALS",
        "items": [
            {"ko": "다시 읽기 또는 다시 쓰기", "en": "Re-reading or re-writing"},
            {"ko": "일상 활동의 반복 (예: 문을 드나들기, 의자에서 일어나 앉기)", "en": "Repeating routine activities (e.g., going in/out, getting up and sitting down)"},
            {"ko": "기타", "en": "Other"}
        ]
    },
    "counting_compulsions": {
        "question_ko": "숫자 세기 강박행동",
        "question_en": "COUNTING COMPULSIONS",
        "items": [
            {"ko": "숫자 세기 강박행동", "en": "Counting compulsions"}
        ]
    },
    "ordering_arranging_compulsions": {
        "question_ko": "정리/배열 강박행동",
        "question_en": "ORDERING/ARRANGING COMPULSIONS",
        "items": [
            {"ko": "정리/배열 강박행동", "en": "Ordering/arranging compulsions"}
        ]
    },
    "hoarding_collecting_compulsions": {
        "question_ko": "저장/수집 강박행동",
        "question_en": "HOARDING/COLLECTING COMPULSIONS",
        "items": [
            {"ko": "저장/수집 강박행동 [취미나 금전적/정서적 가치와 구별]", 
             "en": "Hoarding/collecting compulsions [distinguish from hobbies and interest in valuable objects]"}
        ]
    },
    "miscellaneous_compulsions": {
        "question_ko": "기타 강박행동",
        "question_en": "MISCELLANEOUS COMPULSIONS",
        "items": [
            {"ko": "확인이나 숫자 세기를 제외한 정신적 의례행동", "en": "Mental rituals (other than checking/counting)"},
            {"ko": "과도한 목록 작성", "en": "Excessive listmaking"},
            {"ko": "말하기, 질문, 고백의 필요성", "en": "Need to tell, ask, or confess"},
            {"ko": "만지기, 두드리기, 문지르기 등의 행동 *", "en": "Need to touch, tap, or rub *"},
            {"ko": "깜박임 또는 응시하는 행동 *", "en": "Rituals involving blinking or staring *"},
            {"ko": "자해 또는 타해를 방지하기 위한 행동(확인 행동 제외)", "en": "Measures (not checking) to prevent harm to self/others"},
            {"ko": "의례적 식사 행동 *", "en": "Ritualized eating behaviors *"},
            {"ko": "미신적 행동", "en": "Superstitious behaviors"}
        ]
    }
}

# 평가 문항 및 선택지 데이터 구조 (CYBOCS 평가 척도; obsessions: 문항 1~5, compulsions: 문항 6~10)
cybocs_scale = [
    {
        "id": 1,
        "question_ko": "강박 사고에 소비되는 시간",
        "question_en": "TIME OCCUPIED BY OBSESSIVE THOUGHTS",
        "description_ko": "최근 1주일간 강박 사고가 귀하의 시간에 미친 영향을 평가합니다.",
        "description_en": "How much of your time is occupied by obsessive thoughts over the past week?",
        "options": [
            {"score": 0, "response_text_ko": "전혀 없음", "response_text_en": "None"},
            {"score": 1, "response_text_ko": "하루 1시간 미만 또는 가끔 발생", "response_text_en": "Less than 1 hr/day or occasional"},
            {"score": 2, "response_text_ko": "하루 1~3시간 또는 자주 발생", "response_text_en": "1 to 3 hrs/day or frequent"},
            {"score": 3, "response_text_ko": "하루 3시간 초과 8시간 이하 또는 매우 자주 발생", "response_text_en": "Greater than 3 and up to 8 hrs/day or very frequent"},
            {"score": 4, "response_text_ko": "하루 8시간 초과 또는 거의 지속됨", "response_text_en": "More than 8 hrs/day or near constant"}
        ]
    },
    {
        "id": 2,
        "question_ko": "강박 사고로 인한 기능적 방해",
        "question_en": "INTERFERENCE DUE TO OBSESSIVE THOUGHTS",
        "description_ko": "최근 1주일간 강박 사고가 일상생활(학업, 사회활동 등)에 미친 영향을 평가합니다.",
        "description_en": "How much do your obsessive thoughts interfere with your daily functioning (e.g., school, social)?",
        "options": [
            {"score": 0, "response_text_ko": "전혀 없음", "response_text_en": "None"},
            {"score": 1, "response_text_ko": "약간의 방해 있으나 전반적 수행에는 영향 없음", "response_text_en": "Slight interference but overall performance not impaired"},
            {"score": 2, "response_text_ko": "명확한 방해 있으나 감당 가능함", "response_text_en": "Definite interference but still manageable"},
            {"score": 3, "response_text_ko": "상당한 손상이 있음", "response_text_en": "Substantial impairment"},
            {"score": 4, "response_text_ko": "기능 수행이 마비될 정도임", "response_text_en": "Incapacitating"}
        ]
    },
    {
        "id": 3,
        "question_ko": "강박 사고로 인한 고통의 정도",
        "question_en": "DISTRESS ASSOCIATED WITH OBSESSIVE THOUGHTS",
        "description_ko": "강박 사고가 귀하에게 유발하는 고통이나 불편감의 정도를 평가합니다.",
        "description_en": "How much distress do your obsessive thoughts cause?",
        "options": [
            {"score": 0, "response_text_ko": "전혀 없음", "response_text_en": "None"},
            {"score": 1, "response_text_ko": "크지 않음", "response_text_en": "Not too disturbing"},
            {"score": 2, "response_text_ko": "어느 정도 괴로움", "response_text_en": "Disturbing but manageable"},
            {"score": 3, "response_text_ko": "매우 괴로움", "response_text_en": "Very disturbing"},
            {"score": 4, "response_text_ko": "거의 지속적으로 심한 고통", "response_text_en": "Near constant, disabling distress"}
        ]
    },
    {
        "id": 4,
        "question_ko": "강박 사고에 대한 저항 노력",
        "question_en": "RESISTANCE AGAINST OBSESSIONS",
        "description_ko": "강박 사고가 떠오를 때 이를 무시하거나 저항하려는 노력을 평가합니다.",
        "description_en": "How much effort do you make to resist the obsessive thoughts?",
        "options": [
            {"score": 0, "response_text_ko": "항상 저항하려 함", "response_text_en": "Always resist"},
            {"score": 1, "response_text_ko": "대부분의 시간 저항 시도", "response_text_en": "Try to resist most of the time"},
            {"score": 2, "response_text_ko": "어느 정도 저항함", "response_text_en": "Make some effort to resist"},
            {"score": 3, "response_text_ko": "거의 저항하지 않고 굴복하나 약간의 꺼림칙함 있음", "response_text_en": "Yield to almost all obsessions with slight reluctance"},
            {"score": 4, "response_text_ko": "완전히 자발적으로 굴복함", "response_text_en": "Completely and willingly yield"}
        ]
    },
    {
        "id": 5,
        "question_ko": "강박 사고에 대한 통제력",
        "question_en": "DEGREE OF CONTROL OVER OBSESSIVE THOUGHTS",
        "description_ko": "강박 사고를 중단하거나 다른 데로 전환하는 능력을 평가합니다.",
        "description_en": "How much control do you have over your obsessive thoughts?",
        "options": [
            {"score": 0, "response_text_ko": "완전히 통제 가능", "response_text_en": "Complete control"},
            {"score": 1, "response_text_ko": "노력과 집중으로 대체로 조절 가능", "response_text_en": "Usually able to control with some effort"},
            {"score": 2, "response_text_ko": "가끔 통제 가능", "response_text_en": "Sometimes able to control"},
            {"score": 3, "response_text_ko": "거의 통제 불가능, 주의 전환에 어려움", "response_text_en": "Rarely able to control, difficult to divert attention"},
            {"score": 4, "response_text_ko": "전혀 통제 불가능", "response_text_en": "No control, completely involuntary"}
        ]
    },
    {
        "id": 6,
        "question_ko": "강박 행동에 소비되는 시간",
        "question_en": "TIME SPENT PERFORMING COMPULSIVE BEHAVIORS",
        "description_ko": "최근 1주일간 강박 행동 수행에 소요되는 시간 및 일상 활동에서의 지연 정도를 평가합니다.",
        "description_en": "How much time do you spend performing compulsive behaviors over the past week?",
        "options": [
            {"score": 0, "response_text_ko": "전혀 없음", "response_text_en": "None"},
            {"score": 1, "response_text_ko": "하루 1시간 미만 또는 가끔 수행", "response_text_en": "Less than 1 hr/day or occasional"},
            {"score": 2, "response_text_ko": "하루 1~3시간 또는 자주 수행", "response_text_en": "1 to 3 hrs/day or frequent"},
            {"score": 3, "response_text_ko": "하루 3시간 초과 8시간 이하 또는 매우 자주 수행", "response_text_en": "More than 3 and up to 8 hrs/day or very frequent"},
            {"score": 4, "response_text_ko": "하루 8시간 초과 또는 거의 지속됨", "response_text_en": "More than 8 hrs/day or near constant"}
        ]
    },
    {
        "id": 7,
        "question_ko": "강박 행동으로 인한 기능적 방해",
        "question_en": "INTERFERENCE DUE TO COMPULSIVE BEHAVIOR",
        "description_ko": "강박 행동이 일상생활(학업, 사회활동 등)에 미치는 영향을 평가합니다.",
        "description_en": "How much do your compulsive behaviors interfere with your daily functioning?",
        "options": [
            {"score": 0, "response_text_ko": "전혀 없음", "response_text_en": "None"},
            {"score": 1, "response_text_ko": "약간의 방해 있으나 전반적 수행에는 영향 없음", "response_text_en": "Slight interference but overall performance not impaired"},
            {"score": 2, "response_text_ko": "명확한 방해 있으나 감당 가능함", "response_text_en": "Definite interference but still manageable"},
            {"score": 3, "response_text_ko": "상당한 손상 있음", "response_text_en": "Substantial impairment"},
            {"score": 4, "response_text_ko": "기능 수행이 마비될 정도임", "response_text_en": "Incapacitating"}
        ]
    },
    {
        "id": 8,
        "question_ko": "강박 행동과 관련된 고통의 정도",
        "question_en": "DISTRESS ASSOCIATED WITH COMPULSIVE BEHAVIOR",
        "description_ko": "강박 행동 수행이 중단될 경우 나타날 불안 및 고통의 정도를 평가합니다.",
        "description_en": "How much distress would you experience if you were prevented from performing your compulsions?",
        "options": [
            {"score": 0, "response_text_ko": "전혀 없음", "response_text_en": "None"},
            {"score": 1, "response_text_ko": "약간의 불안", "response_text_en": "Slight anxiety if prevented"},
            {"score": 2, "response_text_ko": "불안 증가하나 감당 가능", "response_text_en": "Anxiety would increase but manageable"},
            {"score": 3, "response_text_ko": "뚜렷하고 매우 괴로운 불안", "response_text_en": "Very disturbing anxiety if interrupted"},
            {"score": 4, "response_text_ko": "활동 수정 시 심각한 불안, 기능 마비", "response_text_en": "Incapacitating anxiety from any intervention"}
        ]
    },
    {
        "id": 9,
        "question_ko": "강박 행동에 대한 저항 노력",
        "question_en": "RESISTANCE AGAINST COMPULSIONS",
        "description_ko": "강박 행동에 대해 어느 정도 저항하려고 노력하는지를 평가합니다.",
        "description_en": "How much effort do you make to resist your compulsive behaviors?",
        "options": [
            {"score": 0, "response_text_ko": "항상 저항함", "response_text_en": "Always try to resist"},
            {"score": 1, "response_text_ko": "대부분의 시간 저항 시도", "response_text_en": "Try to resist most of the time"},
            {"score": 2, "response_text_ko": "어느 정도 저항함", "response_text_en": "Make some effort to resist"},
            {"score": 3, "response_text_ko": "거의 저항하지 않고 굴복하나 약간의 꺼림칙함 있음", "response_text_en": "Yield to almost all compulsions with some reluctance"},
            {"score": 4, "response_text_ko": "완전히 자발적으로 굴복함", "response_text_en": "Completely and willingly yield"}
        ]
    },
    {
        "id": 10,
        "question_ko": "강박 행동에 대한 통제력",
        "question_en": "DEGREE OF CONTROL OVER COMPULSIVE BEHAVIOR",
        "description_ko": "강박 행동을 수행하는 충동과 이를 통제하는 능력을 평가합니다.",
        "description_en": "How strong is the drive to perform the compulsive behavior and how much control do you have?",
        "options": [
            {"score": 0, "response_text_ko": "완전히 통제 가능", "response_text_en": "Complete control"},
            {"score": 1, "response_text_ko": "일정 압박 있으나 대체로 통제 가능", "response_text_en": "Pressure present but generally controllable"},
            {"score": 2, "response_text_ko": "압박이 강해 통제가 어렵지만 어느 정도 가능", "response_text_en": "Strong pressure, control only with difficulty"},
            {"score": 3, "response_text_ko": "매우 강한 충동으로 반드시 수행, 지연 어려움", "response_text_en": "Very strong drive; must be performed, can only delay with difficulty"},
            {"score": 4, "response_text_ko": "전혀 통제 불가능, 충동이 압도적임", "response_text_en": "No control, drive is completely involuntary and overpowering"}
        ]
    }
]

# 메인 함수: 앱 상태(증상 체크리스트 / 평가 문항 / 결과 출력)에 따라 화면 전환
def main():
    st.title("CY-BOCS (어린이판) 평가 웹앱")
    
    # st.session_state 초기화
    if "confirmed" not in st.session_state:
        st.session_state["confirmed"] = False
    if "submitted" not in st.session_state:
        st.session_state["submitted"] = False
    if "selected_symptoms_ko" not in st.session_state:
        st.session_state["selected_symptoms_ko"] = []
    if "selected_symptoms_en" not in st.session_state:
        st.session_state["selected_symptoms_en"] = []
    if "answers" not in st.session_state:
        st.session_state["answers"] = {}  # key: 문항 id, value: 선택한 옵션 인덱스

    # 1단계: 도입 증상 체크리스트 화면
    if not st.session_state["confirmed"]:
        st.header("CY-BOCS 도입 증상 체크리스트")
        st.write("아래 항목에서 해당하는 증상을 선택해주세요.")
        # cybocs_mapping의 각 카테고리별로 체크박스 렌더링
        for category_key, category in cybocs_mapping.items():
            st.subheader(category["question_ko"])
            for idx, item in enumerate(category["items"]):
                # "기타" 항목이면 카테고리 제목의 첫 단어로 항목명을 수정
                display_ko = item["ko"]
                display_en = item["en"]
                if item["ko"] == "기타":
                    cat_keyword_ko = category["question_ko"].split()[0]
                    cat_keyword_en = category["question_en"].split()[0]
                    display_ko = f"기타: {cat_keyword_ko}"
                    display_en = f"Other: {cat_keyword_en}"
                # 고유한 키를 사용하여 체크박스 생성
                selected_item = st.checkbox(display_ko, key=f"{category_key}_{idx}")
                if selected_item:
                    # 중복 저장 방지 후 선택한 항목 저장 (수정된 텍스트 사용)
                    if display_ko not in st.session_state["selected_symptoms_ko"]:
                        st.session_state["selected_symptoms_ko"].append(display_ko)
                        st.session_state["selected_symptoms_en"].append(display_en)
        if st.button("증상 선택 완료"):
            st.session_state["confirmed"] = True

    # 2단계: 평가 문항 화면
    elif not st.session_state["submitted"]:
        st.header("CY-BOCS 평가 문항")
        st.write("아래 문항에 대해 해당하는 선택지를 선택해주세요.")
        for question in cybocs_scale:
            options_list = [option["response_text_ko"] for option in question["options"]]
            selected = st.selectbox(
                f"{question['id']}. {question['question_ko']}\n{question['description_ko']}",
                options_list,
                key=f"q_{question['id']}"
            )
            score_index = options_list.index(selected)
            st.session_state["answers"][question["id"]] = score_index
        if st.button("제출"):
            st.session_state["submitted"] = True

    # 3단계: 결과 출력 화면 (영어로만 출력)
    else:
        st.header("Evaluation Results (CY-BOCS)")
        total_score = 0
        results_text = "Children's Yale-Brown Obsessive Compulsive Scale (CY-BOCS)\n\n"
        for question in cybocs_scale:
            qid = question["id"]
            selected_index = st.session_state["answers"].get(qid, 0)
            total_score += question["options"][selected_index]["score"]
            results_text += f"{qid}. {question['question_en']}\n"
            results_text += f"   ({selected_index}) {question['options'][selected_index]['response_text_en']}\n\n"
        results_text += f"Total Score: {total_score}\n"
        
        # 임상적 해석 함수 (점수 구간에 따라 해석을 제공합니다.)
        def interpret_score(score):
            if score <= 7:
                return "Minimal symptoms (0-7 points)"
            elif score <= 15:
                return "Mild symptoms (8-15 points)"
            elif score <= 23:
                return "Moderate symptoms (16-23 points)"
            elif score <= 31:
                return "Severe symptoms (24-31 points)"
            else:
                return "Extreme symptoms (32-40 points)"
        interpretation = interpret_score(total_score)
        results_text += f"Interpretation: {interpretation}\n\n"
        
        # 선택한 증상(영어) 항목을 하나의 문자열로 결합
        english_symptoms = ", ".join(st.session_state["selected_symptoms_en"]) if st.session_state["selected_symptoms_en"] else "None"
        results_text += f"Selected symptoms (English): {english_symptoms}\n"
        
        # st.markdown을 이용해 코드 블록 형태로 출력 (줄바꿈 적용)
        st.markdown(f"```\n{results_text}\n```")

if __name__ == "__main__":
    main()
