import os
import argparse

def countlines(start, lines=0, header=True, begin_start=None):
    if header:
        print('{:>10} |{:>10} | {:<20}'.format('ADDED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing):
            if thing.endswith('.py'):
                with open(thing, 'r', encoding='utf-8', errors='ignore') as f:
                    newlines = f.readlines()
                    newlines = len(newlines)
                    lines += newlines

                    if begin_start is not None:
                        reldir_of_thing = '.' + thing.replace(begin_start, '')
                    else:
                        reldir_of_thing = '.' + thing.replace(start, '')

                    print('{:>10} |{:>10} | {:<20}'.format(
                            newlines, lines, reldir_of_thing))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isdir(thing):
            lines = countlines(thing, lines, header=False, begin_start=start)

    return lines

def main():
    parser = argparse.ArgumentParser(description='Count lines of code in a repository.')
    parser.add_argument('directory', type=str, help='The directory to scan for code files.')
    parser.add_argument('--file-types', type=str, nargs='+', default=['.py'],
                        help='File types to include in the line count (e.g., .py .js).')
    parser.add_argument('--exclude', type=str, nargs='+', default=[],
                        help='Directories or files to exclude from the line count.')
    args = parser.parse_args()

    # Call your countlines function with the parsed arguments
    countlines(args.directory, file_types=args.file_types)

if __name__ == '__main__':
    main()