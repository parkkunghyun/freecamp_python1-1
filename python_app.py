from email.message import EmailMessage 
# 이메일을 보내고 받기 위해서 필요

import app2 # app.py여도 굳이 py적을 필요 없다
import ssl  
# secure soket layer로서 네트워크로 연결된 컴퓨터 간에 인증되고 (공개키)암호화된 링크를 설정하는 프로토콜이다.

import smtplib # smtp방식으로 보낼거여서 이거 필요

email_sender = 'rudgus4620@gmail.com'
email_password = app2.password

email_receiver = 'nasale8422@vpsrec.com'
# 제목
subject = "Dont forget to subscribe"    
body="""
When you watch a video, please hit subscribe
"""

em = EmailMessage() #인스턴스를 만들었음
em['From']=email_sender # 
em['To'] = email_receiver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context() #

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

# em.as_string() 은 전체 메시지를 평평하게 만든문자열을 반환

# with를 사용하면 이걸 사용하는 동안은 자동으로 smtp와 연결되고
# 끝나면 자동으로 닫힘!

# smtplib.SMTP_SSL(호스트 포트번호 로컬호스트네임 아니면 키파일 아니면 증명방법)
# 465는 메일 전송 프로토콜이다!

# 로컬 SMTP서버가 없어 gmail을 사용하면 되는데 gmail은 SSL을 필수로 사용한다. 
# SMTP connect()메서드가 실행되며 호출에 실패하면 timeout이 발생한다.