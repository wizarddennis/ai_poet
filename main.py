from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from dotenv import load_dotenv
import os

import streamlit as st 
import time

# st.title("시 생성기")
# st.table("'가을'에 대한 시를 생성합니다.")
st.title("_AI 시인 :sunglasses:")
content = st.text_input("'가을'에 대한 시를 만들어줘.", "가을")
st.write("시의 주제:", content)




#load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기

#ChatOpenAI 클라이언트의 인스턴스 생성
llm = ChatOpenAI(api_key=api_key, model='gpt-4o-mini')  # 오픈AI 클라이언트의 인스턴스 생성

#프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 사용자를 도와주는 사업가야."),
    ("user", "{input}"),
])

 # 문자열 출력 파서
output_parser = StrOutputParser()

#LLM 체인 구성
chain = prompt | llm | output_parser
result = chain.invoke({'input':"'가을'에 대한 시를 만들어줘."})
if st.button("시 작성"):
    # st.write("시 작성 클릭")
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)
print(result)


