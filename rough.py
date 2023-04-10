from queue import Queue

# Create queues for students and teachers
students_queue = Queue()
teachers_queue = Queue()

# Function to issue books to visitors
def issue_book(visitor):
    if not students_queue.empty() and visitor == "teacher":
        print("Servicing teacher...")
        teachers_queue.get()
    elif not teachers_queue.empty() and visitor == "student":
        print("Servicing student...")
        students_queue.get()
    else:
        print("No visitors in queue.")

# Simulate visitors entering the library and joining the appropriate queue
students_queue.put("student1")
teachers_queue.put("teacher1")
students_queue.put("student2")
teachers_queue.put("teacher2")

# Process issuing of books
issue_book("teacher")
issue_book("student")
issue_book("teacher")
issue_book("student")
issue_book("student")

# Output remaining visitors in the queues
print("Students in queue:", list(students_queue.queue))
print("Teachers in queue:", list(teachers_queue.queue))