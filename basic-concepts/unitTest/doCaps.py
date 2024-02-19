def cap_text(text):
    # text.capitalize()
    if text is None:
        return None
    capitalize = ''

    try:
        capitalize = text.title()
    except:
        raise TypeError("Business Error Message : ABC123454 : Incorrect Type passed - Not a String")

    return capitalize
