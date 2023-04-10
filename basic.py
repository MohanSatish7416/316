import threading
import random

pen_sem = threading.Semaphore(0)
paper_sem = threading.Semaphore(0)
qp_sem = threading.Semaphore(0)

num_students = int(input("Enter the number of students: "))
num_assignments = int(input("Enter the number of assignments each student needs to complete: "))


def teacher():
    for i in range(num_students * num_assignments):
        item1 = random.randint(1, 3)
        item2 = random.randint(1, 3)
        while item2 == item1:
            item2 = random.randint(1, 3)
        if item1 == 1 and item2 == 2:
            print("Teacher placed pen and paper on table.")
            pen_sem.release()
            paper_sem.release()
        elif item1 == 2 and item2 == 1:
            print("Teacher placed pen and paper on table.")
            pen_sem.release()
            paper_sem.release()
        elif item1 == 1 and item2 == 3:
            print("Teacher placed pen and question paper on table.")
            pen_sem.release()
            qp_sem.release()
        elif item1 == 3 and item2 == 1:
            print("Teacher placed pen and question paper on table.")
            pen_sem.release()
            qp_sem.release()
        elif item1 == 2 and item2 == 3:
            print("Teacher placed paper and question paper on table.")
            paper_sem.release()
            qp_sem.release()
        elif item1 == 3 and item2 == 2:
            print("Teacher placed paper and question paper on table.")
            paper_sem.release()
            qp_sem.release()


def student(num):
    for i in range(num_assignments):
        if num == 1:
            pen_sem.acquire()
            paper_sem.acquire()
            print("Student {} is making assignment {}.".format(num, i + 1))
            # Assignment making code here
            print("Student {} completed assignment {}.".format(num, i + 1))
            qp_sem.release()
        elif num == 2:
            pen_sem.acquire()
            qp_sem.acquire()
            print("Student {} is making assignment {}.".format(num, i + 1))
            # Assignment making code here
            print("Student {} completed assignment {}.".format(num, i + 1))
            paper_sem.release()
        elif num == 3:
            paper_sem.acquire()
            qp_sem.acquire()
            print("Student {} is making assignment {}.".format(num, i + 1))
            # Assignment making code here
            print("Student {} completed assignment {}.".format(num, i + 1))
            pen_sem.release()


# Create and start the threads
t = threading.Thread(target=teacher)
t.start()

students = []
for i in range(num_students):
    s = threading.Thread(target=student, args=(i + 1,))
    students.append(s)
    s.start()

for s in students:
    s.join()