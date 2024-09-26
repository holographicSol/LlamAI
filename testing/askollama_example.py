""" AI Driven Module Example Use - Written by Benjamin Jack Cullen """

import askollama


def function_true():
    """ basically the only function that would need to be written because ollama will process the data """
    print('executing: function_true')


def function_false():
    """" basically the only function that would need to be written because ollama will process the data """
    print('executing: function_false')


def example_function_1():
    print('')
    print('example 1: using matrix file')
    config_file = './config.dat'
    if askollama.get_matrix(config_file) is True:
        if bool(askollama.ollama()) is True:
            function_true()
        elif bool(askollama.ollama()) is False:
            function_false()


def example_function_2():
    print('\nexample 2: using hardcoded matrix')
    askollama.matrix =\
    [[
        {
            'COMMAND':       'ping -n 4 8.8.8.8',
            'MAIN_INTERVAL': 3,
            'QUERY':         'Answer by responding exactly with wither True of False (like a pythonic returned bool).'
                             'According to the ping, is the packet loss 0%?'
        }
    ]]
    if bool(askollama.ollama()) is True:
        function_true()
    elif bool(askollama.ollama()) is False:
        function_false()


example_function_1()
example_function_2()
