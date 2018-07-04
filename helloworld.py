



import re
# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


def get_cleaned_english_sentence(raw_english_sentence):
    # """
    # Input:
    #     - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    # Output:
    #     - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.get_cleaned_english_sentence("This is Gachon!!")
    #     'This is Gachon'
    #     >>> mc.get_cleaned_english_sentence("Is this Gachon?")
    #     'Is this Gachon'
    #     >>> mc.get_cleaned_english_sentence("How are you?")
    #     'How are you'
    #     >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
    #     'Fine Thank you and you'
    # """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    splitted_letters=[i for i in raw_english_sentence if not i =="." if not i =="," if not i =="!" if not i =="?"]
    joined="".join(splitted_letters)
    result= joined.strip()

    return result
    # ==================================



def encoding_character(english_character):
#     """
#     Input:
#         - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
#     Output:
#         - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
#     Examples:
#         >>> import morsecode as mc
#         >>> mc.encoding_character("G")
#         '--.'
#         >>> mc.encoding_character("A")
#         '.-'
#         >>> mc.encoding_character("C")
#         '-.-.'
#         >>> mc.encoding_character("H")
#         '....'
#         >>> mc.encoding_character("O")
#         '---'
#         >>> mc.encoding_character("N")
#         '-.'
#     """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    result =""
    for k, v in morse_code_dict.items():
        if k == english_character:
            result=v


    return result
    # ==================================


def encoding_sentence(english_sentence):

    cleaned_sentence = get_cleaned_english_sentence(english_sentence)
    result = ""
    sentence=[]
    list1 = cleaned_sentence.split(" ")
    for i in list1:
        splitted_list = i.split()
        for j in splitted_list:
            k_num=0;
            for k in j:
                print(k)
                k_num+=1;
                morse = encoding_character(k.upper())
                sentence.append(morse)
                if(k_num != j[len(j)-1]):
                    print(k_num)
                    sentence.append(" ")
            sentence.append(" ")

    joined = "".join(sentence)
    striped_result = joined.strip()
    result = striped_result


    return result


print(encoding_sentence("SOS"))
