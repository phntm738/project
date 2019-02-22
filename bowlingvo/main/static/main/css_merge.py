

fnames = ['variables', 'main', 'header', 'content/authorization', 'content/profile', 'content/index', 'content/language_page', 'content/avatar_change']


def merge():
    result = open('index.css', 'w')
    for fname in fnames:
        full_name = 'styles/' + fname + '.css'
        f = open(full_name)
        result.write('/*-----'+fname+'-----*/\n')
        for line in f:
            result.write(line)
        result.write('/*----/'+fname+'-----*/\n\n')
        f.close()
    result.close()


if __name__ == '__main__':
    merge()
