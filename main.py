#from dotenv import load_dotenv
#load_dotenv()

#from langchain.llms import OpenAI
#llm = OpenAI()
#result = llm.predict('내가 좋아하는 동물은 ')
#print(result)

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

#content = "조깅"
#result = chat_model.predict(content + "에 대한 시를 써줘")
#print(result)

import streamlit as myst

myst.title('인공지능 시인')
title = myst.text_input('시의 주제를 입력해 주세요')
#myst.write('시의 주제는', title)
if myst.button('시 작성 요청하기'):
    with myst.spinner('시 작성 중...'):
        result = chat_model.predict(title + "에 대한 시를 써줘")
        myst.write(result)


