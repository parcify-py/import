from func import *

def main():
    word = input("Enter the word: ")
    count = int(input("Enter count: "))
    f_print(word,count)
    first_p(word.replace(' ',''))
    
  
if __name__ == '__main__':
    main()