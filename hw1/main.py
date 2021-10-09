import bfs as bfs
import hc as hc
import csp as csp


def main():
    print("Solve N-queens problem with 3 algorithms")
    f = open("input.txt", 'r')

    while True:
        line = f.readline()
        if not line:
            break
        n, algo = line.split()
        if algo == "bfs":
            bfs.bfs(n)
        elif algo == "hc":
            hc.hc(n)
        elif algo == "csp":
            csp.csp(n)


if __name__ == "__main__":
    main()
