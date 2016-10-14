def main():

    total = 0.0
    length = 0.0
    try:
        filename = raw_input('Enter a file name: ')
        infile = open(filename, 'r')
        for line in infile:
            print line.rstrip("\n")
            amount = float(line.rstrip("\n"))
            total += amount
            length = length + 1


        average = total / length

        #Close the file
        infile.close()

        #Print the amount of numbers in file and average
        print 'There were', length, 'numbers in the file.'
        print format(average, ',.2f')
    except IOError:
        print 'An error occurred trying to read the file.'
    except ValueError:
        print 'Non-numeric data found in the file'
    except:
        print('An error has occurred')
main()