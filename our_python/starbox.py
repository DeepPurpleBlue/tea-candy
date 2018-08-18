def find_longest_word(list_of_words):
    longest=0
    for i in list_of_words:
        if len(i) > longest:
            longest=len(i)
    return longest

def star_string(func,length):
    strrr = ''
    for i in range(0,length):
        strrr += '*'
    func(strrr)

def element_string(element,func,length):
    element_size = len(element)
    strrr = '* {}'.format(element)
    x = length - element_size
    for i in range(0,x):
        strrr += ' '
    strrr += ' *'
    func(strrr)


def print_box(list_of_items):
    
    longest = find_longest_word(list_of_items)
    exact_length=longest+4
    star_string(print,exact_length)
    for i in list_of_items:
        element_string(i,print,longest)
    star_string(print,exact_length)

def main():
    #a = input()
    #list_a = list(a)
    list_a = ['akbar', '123123', 'h', 'س']
    print_box(list_a)

if __name__ == '__main__':
    main()