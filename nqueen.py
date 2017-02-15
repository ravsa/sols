import copy


class Queen(object):
    __BOARD = list()

    def __init__(self, num_of_queens=4):
        self.num_of_queens = num_of_queens
        self.solutions = list()
        self.flag = False

    def queen_is_safe(self, row, col):
        for i, j in self.__BOARD:
            if row is i or col is j:
                return False  # check vertical and horizontal
            elif abs(row - i) is abs(col - j):
                return False  # check diagonally
        return True

    def place(self, position):
        self.__BOARD.append(position)

    def remove(self, position):
        self.__BOARD.remove(position)

    def place_queens(self, row):
        if row >= self.num_of_queens:
            return True
        else:
            for col in xrange(self.num_of_queens):
                if self.queen_is_safe(row, col):
                    self.place((row, col))
                    if self.place_queens(row + 1):
                        return True
                    self.remove((row, col))
            return False

    def total_solutions(self, row):
        if row >= self.num_of_queens:
            self.solutions.append(copy.copy(self.__BOARD))
        else:
            for col in xrange(self.num_of_queens):
                if self.queen_is_safe(row, col):
                    self.place((row, col))
                    self.total_solutions(row + 1)
                    self.remove((row, col))

    def display(self, action="place_queens"):
        if action is "place_queens":
            self.place_queens(0)
            for row in xrange(self.num_of_queens):
                for col in xrange(self.num_of_queens):
                    if (row, col) in self.__BOARD:
                        print "Q",
                    else:
                        print '-',
                print
        elif action is "num_of_solutions":
            if not self.flag:
                self.total_solutions(0)
                self.flag = True
            print "Number Of Different Solutions: {}".format(len(self.solutions))

        elif action is "print_solutions":
            if not self.flag:
                self.total_solutions(0)
                self.flag = True
            for index, solution in enumerate(self.solutions, 1):
                print "Solutions: %d" % index
                for row in xrange(self.num_of_queens):
                    for col in xrange(self.num_of_queens):
                        if (row, col) in solution:
                            print "Q",
                        else:
                            print '-',
                    print
                print


Q = Queen(num_of_queens=8)
#  Q.display(action="print_solutions")
#  Q.display(action="num_of_solutions")
Q.display(action="place_queens")
