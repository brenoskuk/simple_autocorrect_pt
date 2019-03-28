#important https://docs.python.org/3/library/stdtypes.html#string-methods
import string

def delete_punctuation(text_input):
    return text_input.translate(str.maketrans('', '', string.punctuation))


##str.find(str, beg=0, end=len(string))

#if remove_whitespace = 1 deletes one more character IF it's a whitespace
def delete_specific(text_input,specific, remove_whitespace = False):
    trim_size = len(specific)
    pos = text_input.find(specific)

    if (remove_whitespace and pos >= 0 and len(text_input) > pos+trim_size + 1) :
        if ( pos >= 0 and remove_whitespace == True and text_input[pos+trim_size] == " " ):
            new_text = text_input[:pos]+text_input[pos+trim_size+1:]
            return new_text
        elif (pos >= 0):
            new_text = text_input[:pos]+text_input[pos+trim_size:]
            return new_text
        else:
            return text_input
    else:
        if (pos >= 0):
            new_text = text_input[:pos]+text_input[pos+trim_size:]
            return new_text
        else:
            return text_input



