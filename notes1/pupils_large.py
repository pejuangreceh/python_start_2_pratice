import time
class Pupil:
    def __init__(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

Pupils_amount = 0
Best_pupils = []
Sum = 0

current_amount = 0
start_time = time.time()
with open("pupil_large.txt", "r") as file:
    for line in file:
        data = line.split(" ")
        data_pupil = Pupil(data[0], data[1], int(data[2]))

        if data_pupil.Mark == 5:
            Best_pupils.append(data_pupil.Surname)
        Pupils_amount += 1 
        Sum += int(data_pupil.Mark)

        current_amount += 1

print("Average grade:", (Sum/Pupils_amount), "\n\nTop students:")
for pupil in Best_pupils:
     print(pupil)

print("Runtime: ", (time.time()-start_time), "seconds")