#Find the difference between sum of the square and square of the sums for the first
#100 numbers

def difference(n):
    squareOfSum = (n*(n+1)/2)**2
    sumofSquare = n*(n+1)*(2*n+1)/6
    print squareOfSum - sumofSquare
def main():
    difference(100)

if __name__ == "__main__":
    main()