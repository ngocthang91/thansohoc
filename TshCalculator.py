
import re
import sys

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}


tsh_char_to_number = [
    'AJS',    # 1
    'BKT',    # 2
    'CLU',    # 3
    'DMV',    # 4
    'ENW',    # 5
    'FOX',    # 6
    'GPY',    # 7
    'HQZ',    # 8
    'IR', # 9
]
class TshCalculator:
    def __init__(self) -> None:
        pass

    def tsh_get_index_char(self, char):
        for elem in tsh_char_to_number:
            if (char in elem):
                return str(tsh_char_to_number.index(elem) + 1)
        
        return ""

    def tsh_convert_vietnamese_to_nonvietnamese(self, text):
        """
        Convert from 'Tiếng Việt có dấu' thanh 'Tieng Viet khong dau'
        text: input string to be converted
        Return: string converted
        """
        output = text
        for regex, replace in patterns.items():
            output = re.sub(regex, replace, output)
            # deal with upper case
            output = re.sub(regex.upper(), replace.upper(), output)
        return output

    def tsh_convert_text_to_number(self, strText):
        convertText = strText.replace(" ", "").upper()
        numText = ""
        for i in range(len(convertText)):
            numText += str(self.tsh_get_index_char(convertText[i]))

        return numText

    def tsh_convert_name_to_number(self, strName):
        convertNums = ""
        unSignText = self.tsh_convert_vietnamese_to_nonvietnamese(strName)
        print("unSignText: " + str(unSignText))
        convertNums = self.tsh_convert_text_to_number(unSignText)
        print("convertNums: " + str(convertNums))
        if (convertNums != None):
            return str(convertNums)
        else:
            return ""

    def tsh_convert_birthday_to_number(self, strBirthDay):
        convertedText = strBirthDay.replace("/", "")
        convertedText = convertedText.replace("-", "")
        return convertedText

    def tsh_convert_name_and_birthday_to_number(self, strName, strBirthDay):
        outputText = ""
        arrayName = self.tsh_convert_name_to_number(strName)
        arrayBirthDay = self.tsh_convert_birthday_to_number(strBirthDay)
        if (arrayName != None):
            outputText += str(arrayName)
        if (arrayBirthDay != None):
            outputText += str(arrayBirthDay)
        return outputText


