class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # check whether any student still in the queue prefers the top sandwich
        # also stops when all students are gone
        """ QUEUE (O(n^2)) SO SLOW
        while len(students) > 0 and sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                stud = students.pop(0)
                students.append(stud)
        return len(students)
        """
        # can rearrange students in an array
        # only Sandwiches needs a strict pointer
        ones = 0
        zeroes = 0
        for student in students:
            if student == 1:
                ones += 1
            else:
                zeroes += 1
        
        for i in range(len(sandwiches)):
            if sandwiches[i] == 1 and ones != 0:
                ones -= 1
            elif sandwiches[i] == 0 and zeroes != 0:
                zeroes -= 1
            else:
                break

        return ones + zeroes