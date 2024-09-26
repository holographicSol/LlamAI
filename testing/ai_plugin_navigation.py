""" AI Driven Application Real-Time Data Plugin - Written by Benjamin Jack Cullen 

This application provides satellite and inertial data to the AI, which can then be queried. This makes the AI aware of
its location on earth, trajectory, and the ability to locate of potentially anything in time.

"""

import os.path
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
            'COMMAND':       'C:/Users/Benjamin/PycharmProjects/OLLAMA/dist/com_listen.exe',
            'QUERY':         'I am plugging you into my satellite and inertial navigation system.'
                             'I will provide a sentence and I will tell you how to interpret the sentence.'
                             'The sentence is comprised of comma delimited elements.'
                             'The fourth element is absolute latitude.'
                             'The fifth element is absolute longitude.'
                             'The intention now is for you to geolocate the provided coordinates!'
        }
    ]]
    result = askollama.ollama()
    print('result:', result)

    # print('repr(str(result)):', repr(str(result)))
    # if 'False' in str(result):
    #     function_false()
    # elif 'True' in str(result):
    #     function_true()


template_example()
