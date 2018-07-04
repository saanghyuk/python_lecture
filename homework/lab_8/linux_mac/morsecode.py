# -*- coding: utf8 -*-

import re
# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    # """
    # Input:
    #     - user_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #     - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
    #       그렇지 않을 경우 False를 반환함
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.is_help_command("H")
    #     True
    #     >>> mc.is_help_command("Help")
    #     True
    #     >>> mc.is_help_command("Half")
    #     False
    #     >>> mc.is_help_command("HeLp")
    #     True
    #     >>> mc.is_help_command("HELLO")
    #     False
    #     >>> mc.is_help_command("E")
    #     False
    # """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    lower_case = user_input.lower()
    if(lower_case=='h' or lower_case=="help"):
        result = True
    else:
        result = False

    return result
    # ==================================


def is_validated_english_sentence(user_input):
    # """
    # Input:
    #     - user_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #     - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
    #       1) 숫자가 포함되어 있거나,
    #       2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
    #       3) 영어와 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.is_validated_english_sentence("Hello 123")
    #     False
    #     >>> mc.is_validated_english_sentence("Hi!")
    #     True
    #     >>> mc.is_validated_english_sentence(".!.")
    #     False
    #     >>> mc.is_validated_english_sentence("!.!")
    #     False
    #     >>> mc.is_validated_english_sentence("kkkkk... ^^;")
    #     False
    #     >>> mc.is_validated_english_sentence("This is Gachon University.")
    #     True
    # """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    list = [i for i in user_input]
    result =""
    not_blank_list = [i for i in list if not i == " " if not i == "?" if not i =="." if not i =="," if not i =="!"]
    join_str = "".join(not_blank_list)


    def hasNumbers(inputString):
        return bool(re.search(r'\d', inputString))
    def hasSpecials(inputString):
        return bool(re.search( '[^A-Za-z0-9]', inputString))

    if( hasNumbers(join_str)== True):
        result = False
    else:
        if(hasSpecials(join_str)==True):
            result = False
        else:
            if(len(join_str)==0):
                result = False
            else:
                result=True

    return result
    # ==================================


def is_validated_morse_code(user_input):
    # """
    # Input:
    #     - user_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #     - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
    #       1) "-","."," "외 다른 글자가 포함되어 있는 경우
    #       2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.is_validated_morse_code("..")
    #     True
    #     >>> mc.is_validated_morse_code("..-")
    #     True
    #     >>> mc.is_validated_morse_code("..-..")
    #     False
    #     >>> mc.is_validated_morse_code(". . . .")
    #     True
    #     >>> mc.is_validated_morse_code("-- -- -- --")
    #     True
    #     >>> mc.is_validated_morse_code("!.1 abc --")
    #     False
    # """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = ""

    morseMatch=([i for i in get_morse_code_dict().values()])
    splitted=user_input.split()
    same_list = [j for i in morseMatch for j in splitted if i==j]
    #

    if(len(same_list) == len(splitted)):
        result = True
    else:
        result = False

    return result
    # ==================================



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


def decoding_character(morse_character):
    # """
    # Input:
    #     - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    # Output:
    #     - Morse Code를 알파벳으로 치환함 값
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.decoding_character("-")
    #     'T'
    #     >>> mc.decoding_character(".")
    #     'E'
    #     >>> mc.decoding_character(".-")
    #     'A'
    #     >>> mc.decoding_character("...")
    #     'S'
    #     >>> mc.decoding_character("....")
    #     'H'
    #     >>> mc.decoding_character("-.-")
    #     'K'
    # """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()

    result=""
    for k, v in morse_code_dict.items():
        if v == morse_character:
            result=k

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


def decoding_sentence(morse_sentence):
    # """
    # Input:
    #     - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    # Output:
    #     - 모스부호를 알파벳으로 변환한 문자열
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.decoding_sentence("... --- ...")
    #     'SOS'
    #     >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
    #     'GACHON'
    #     >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
    #     'I LOVE YOU'
    #     >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
    #     'YOU ARE F'
    # """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = ""
    sentence=[]
    list1 = morse_sentence.split("  ")
    for i in list1:
        splitted_list = i.split()
        for j in splitted_list:
            char = decoding_character(j)
            sentence.append(char)
        sentence.append(" ")
    result="".join(sentence)
    return result.strip()
    # ==================================


def encoding_sentence(english_sentence):
    # """
    # Input:
    #     - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    # Output:
    #     - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
    #       단 양쪽 끝에 빈칸은 삭제한다.
    # Examples:
    #     >>> import morsecode as mc
    #     >>> mc.encoding_sentence("HI! Fine, Thank you.")
    #     '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
    #     >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
    #     '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
    #     >>> mc.encoding_sentence("We Are Gachon")
    #     '.-- .  .- .-. .  --. .- -.-. .... --- -.'
    #     >>> mc.encoding_sentence("Hi! Hi!")
    #     '.... ..  .... ..'
    # """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정

    cleaned_sentence = get_cleaned_english_sentence(english_sentence)
    result = ""
    sentence=[]
    list1 = cleaned_sentence.split(" ")
    for i in list1:
        splitted_list = i.split()
        for j in splitted_list:
            k_num=0;
            for k in j:
                k_num+=1;
                morse = encoding_character(k.upper())
                sentence.append(morse)
                if(k_num != j[len(j)-1]):

                    sentence.append(" ")
            sentence.append(" ")

    joined = "".join(sentence)
    striped_result = joined.strip()
    result = striped_result


    return result
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    replay=True
    while replay:
        input_message = input("Input your message(H - Help, 0 - Exit): ")
        if(is_help_command(input_message)):
            print(get_help_message())
            continue;
        else:
            if(is_validated_english_sentence(input_message)):
                print(encoding_sentence(input_message))
            elif(is_validated_morse_code(input_message)):
                print(decoding_sentence(input_message))
            elif(input_message =="0"):
                break;
            else:
                print("Wrong Input")

    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
