def get_camel_case(pothole_case):
    """
    This is a much improved function!
    """
    # Replace underscores with spaces temporarily
    camel_case = pothole_case.replace('_', ' ')

    # Use a call to title to capitalize the first letter of each word
    camel_case = camel_case.title()

    # Make the first letter only lowercase
    camel_case = camel_case[0].lower() + camel_case[1:]

    # Remove the spaces and return the string
    return camel_case.replace(' ', '')

if __name__ == '__main__':
    """
    Note: Once the assertion passes, you're good!
    """
    assert 'thisIsACamelCasePhrase' == get_camel_case('this_is_a_camel_case_phrase'), \
        'Function returned "{}"'.format(get_camel_case('this_is_a_camel_case_phrase'))