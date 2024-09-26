""" AI Driven Application Template - Written by Benjamin Jack Cullen """

import askollama


def function_true():
    """ action: can be anything you like, even sending the response out to an embedded device. """
    print('executing: function_true')


def function_false():
    """ action: can be anything you like, even sending the response out to an embedded device. """
    print('executing: function_false')


def template_example():
    """
    command: can be anything you like, even retrieving information from an embedded device.
    query: query data yielded by command.
    """
    print('')
    askollama.matrix =\
    [[
        {
            'COMMAND':       'ping -n 1 8.8.8.8',
            'QUERY':         'Answer by responding exactly with wither True of False (like a returned pythonic bool).'
                             'According to the ping, am I online?'
        }
    ]]
    result = askollama.ollama()
    # print('result:', result)
    # print('repr(str(result)):', repr(str(result)))
    if 'False' in str(result):
        function_false()
    elif 'True' in str(result):
        function_true()


template_example()
