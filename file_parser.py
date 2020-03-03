import sys

def parse_file(infile):
    
    f = open(f'{infile}', 'r')

    write_file = open('words.txt', 'w')

    lines = f.readlines()

    line_num = 1
    for line in lines:
        words = line.split(' ')
        
        for word in words:
            if word[-1:] == '\n':
                write_file.write(f'{word[:-1]} : {line_num}')
            else:
                write_file.write(f'{word}: {line_num}')
            write_file.write('\n')
        line_num += 1

    f.close()
    write_file.close()


if __name__ == "__main__":
    
    parse_file(sys.argv[1])
