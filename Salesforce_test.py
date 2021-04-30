file = open(("source.txt"), "r")  # (os.path.join(local_dir, "source.txt"), "r") as file:
read_file_to_list = file.read().split('\n') #['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8', 'row 9', 'row 10']
rows_count = len(read_file_to_list) #10
recur_fibo = lambda n: n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2)
fibo_numbers = ([recur_fibo(i) for i in range(rows_count)]) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
result_reversed_string = [i[::-1] for i in read_file_to_list if read_file_to_list.index(i) + 1 in fibo_numbers] #['1 wor', '2 wor', '3 wor', '5 wor', '8 wor']
cuted_row = [(i[(i.rfind(' ') + 1):]) for i in result_reversed_string] #['wor', 'wor', 'wor', 'wor', 'wor']


with open("output.txt", "x") as newfile:
    for count, value in enumerate(cuted_row, start=1):
        newfile.write(f'{(count)} {"".join(value)}\n')

    newfile.close()
file.close()
