from madlib_cli.madlib import madlib


def test_go():
    actual = madlib()
    assert actual == """
    Welcome to the Madlib cli app!
    Prompts will ask you to input
    certain types of words. For example,
    if the prompt asks for a color you
    might type "red". 
    After you type your response press
    enter to continue.
    After all prompts have been entered, 
    the finished madlib will be displayed 
    and saved as a text file. Have fun!
    """