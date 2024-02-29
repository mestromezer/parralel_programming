import random

def create_data_files(filename_1, size):
    random.seed()
    f1 = open(filename_1, "a+")
    for i in range(size*size):
        if (i != size*size - 1):
            f1.write(str(random.randint(0, 10)) + "\n")
        else:
            f1.write(str(random.randint(0, 10)))
    f1.close()



if __name__ == "__main__":
    list_size = [10, 50, 100, 500, 600, 700, 800, 900, 1000]
    list_folder_name = ["E:\\PP\\1\\Python\\data_1\\", "E:\\PP\\1\\Python\\data_2\\"]
    for i in list_folder_name:
        for j in list_size:
            create_data_files(i + str(j) + ".txt", j)
