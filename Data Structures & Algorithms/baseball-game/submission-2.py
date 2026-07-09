class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use push, pop, peek
        # + : sum previous 2 scores
        # C : remove previous score
        # D : double the previous score

        scores = []
        
        for i in range(len(operations)):
            if operations[i] == "C":
                if scores != []:
                    scores.pop()

            elif operations[i] == "+":
                if len(scores) >= 2:
                    first = scores[-1]
                    second = scores[-2]
                    scores.append(first+second)

            elif operations[i] == "D":
               if len(scores) >= 1:
                    last = scores[-1]
                    scores.append(last*2)

            else:
                integer = int(operations[i])
                scores.append(integer)

        return sum(scores)
