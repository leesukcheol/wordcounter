from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text= request.GET['fulltext']
    #home.html에서 textarea의 이름이 fulltext이니까.
    #text라는 파이썬 변수에 home.html의 텍스트에어리어 코드 원문 내용이 담김.
    #html에서 파이썬 변수를 쓰려면 템플릿 뭐시기..{}..이거인듯
    #result.html으로!
    words= text.split()
    word_dictionary= {}
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    return render(request, 'result.html', {'full':text, 'total': len(words), 'dictionary': word_dictionary.items()})
# render라는 함수는 매개변수가 세개까지.
# 1. 리퀘스트(거의 고정) 2. 템플릿 3. (선택) 딕셔너리형 변수
# 왼쪽에는 키값, 오른쪽엔 밸류.<- 딕셔너리 기억나제?
#items()는 (키:밸류) 키:밸류 키:밸류 쌍으로 넘기는 것.

