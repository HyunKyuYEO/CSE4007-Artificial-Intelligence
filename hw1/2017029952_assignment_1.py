import bfs as bf
import hc as hc

def main():
    print("Solve N-queens problem with 3 algorithms")
    f = open("input.txt", 'r')

    while True:
        line = f.readline()
        n, algo = line.split()
        if algo == "bfs":
            bf.bfs(n)
        elif algo == "hc":
            hc.hc(n)
"""     elif algo == "csp":
            csp(n)
        """

if __name__ == "__main__":
    main()
