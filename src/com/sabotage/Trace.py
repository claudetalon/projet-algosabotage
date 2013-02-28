def writeIntoFile(trace):
    fichier = open('executiontrace.txt', 'a')

    if 'begin' in trace :
        fichier.write('\n--NEW EXECUTION--\n')
    elif 'end' in trace :
        fichier.write('--END OF EXECUTION--\n')
    else :
        fichier.write(trace + '\n')
    print(trace)
    fichier.close()
