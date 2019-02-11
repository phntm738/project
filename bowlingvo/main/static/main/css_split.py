import os
import re
start_tag = r'/\*-----[a-z/_]{1,}-----\*/\n'
end_tag = r'/\*----/[a-z/_]{1,}-----\*/\n'
directory = 'split_styles'


def split():
    if not os.path.exists(directory):
        os.mkdir(directory)
    if not os.path.exists(directory + '/content'):
        os.mkdir(directory + '/content')
    to_split = open('index.css')
    f = open('index.css')
    for line in to_split:
        if re.match(end_tag, line):
            f.close()
        elif re.match(start_tag, line):
            if f:
                f.close()
            fname = line[7:-8] + '.css'
            if '/' in fname:
                fname = list(fname.split('/'))[1]
                f = open(directory + '/content/' + fname, 'w')
            else:
                f = open(directory + '/' + fname, 'w')
        else:
            if line == '\n' and f.closed:
                continue
            f.write(line)


if __name__ == '__main__':
    split()
