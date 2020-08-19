import re

def madlib():
    print("""
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
    """)
    temp = ""
    with open('template.txt', 'r') as temp:
        temp = temp.read()
    regex1 = '{([^}]*)}'
    regex2 = '({[^}]*})'
    matches = re.findall(regex1, temp)
    for i in range(len(matches)):
        m = re.search(regex2, temp)
        print(matches[i])
        temp = temp[:m.start()] + input() + temp[m.end():]
        print('\n')
    print(temp)
    with open('madlib-response.txt', 'w+') as result:
        result.write(temp)
    return temp

if __name__ == '__main__':
    madlib()