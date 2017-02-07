def get_camel_case(pothole_case):
    """
    This is a buggy function. Find the bugs and fix them! Hint: try placing a print statement after each statement,
    to check if the string is in the state that you would expect as per the comment.
    """
    # Replace underscores with spaces temporarily
    camel_case = pothole_case.replace(' ', '_')

    # Use a call to title to capitalize the first letter of each word
    camel_case = pothole_case.title()

    # Make the first letter only lowercase
    camel_case = camel_case[0].upper() + camel_case[:1]

    # Remove the spaces and return the string
    return print(camel_case.replace(' ', ''))

if __name__ == '__main__':
    """
    Note: Once the assertion passes, you're good!
    """
    assert 'thisIsACamelCasePhrase' == get_camel_case('this_is_a_camel_case_phrase'), \
        'Function returned "%s"'%get_camel_case('this_is_a_camel_case_phrase')