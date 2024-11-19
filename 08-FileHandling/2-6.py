'''6. Na podstawie pliku txt, zapisz części zawartości do plików o nazwach*1, *2, itd.'''

with open("shopping_list.txt") as f:
    lines = f.readlines()
    for i in range(1, len(lines)+1):
        namefile = "shopping_list" + str(i)
        with open(namefile, 'a') as f2:
            count = 0
            for line in lines:
                f2.write(line)
                count += 1
    
## do pomyslenia