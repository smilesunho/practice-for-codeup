#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
정보검색실에서 노트북으로 문서를 작성하던 광곽이는 갑자기 어떠한 파일의 확장자를 보고 이 확장자가 어떤 파일인지 잊어버렸다.
광곽이가 파일.확장자를 입력하면 이게 어떤 프로그램인지 알 수 있도록 도와주자.
광곽이는 대소문자에 예민하다!
확장자 종류  
.dib : Paint.Picture  
.doc : Word.Document.8  
.docx : Word.Document.12  
.htm : htmfile  
.html : htmlfile  
.hwp : Hwp.Document.96  
.hwpx : Hwp.Document.hwpx.96  
.hwt : Hwp.Document.hwt.96  
.jpe, .jpeg, .jpg : jpegfile  
.ppt : PowerPoint.Show.8  
.pptx : PowerPoint.Show.12  
.pptxml : powerpointxmlfile

'''
a,b=input().strip().split(".")
b=str(b)
if b=="dib":
    print("Paint.Picture")
elif b=="doc":
    print("Word.Document.8")
elif b=="docx":
    print("Word.Document.12")
elif b=='htm':
    print('htmfile')
elif b=="html":
    print("htmlfile")
elif b=="hwp":
    print("Hwp.Document.96")
elif b=="hwpx":
    print("Hwp.Document.hwpx.96")
elif b=="hwt":
    print("Hwp.Document.hwt.96")
elif b=="jpe" or b=="jpeg" or b=='jpg':
    print('jpegfile')
elif b=='ppt':
    print("PowerPoint.Show.8")
elif b=='pptx':
    print("PowerPoint.Show.12")
elif b=='pptxml':
    print("powerpointxmlfile")
    





        
        


# In[ ]:




