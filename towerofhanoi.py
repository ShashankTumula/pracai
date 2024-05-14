def towerofhanoi(n, source, target, aux):
    if n == 1:
        print("Moving 1 disk from", source, "to", target)
        return
    towerofhanoi(n - 1, source, aux, target)
    print("Moving", n, "disk from", source,"to", target)
    towerofhanoi(n - 1, aux, target, source)

num = int(input("Enter number of stacks :"))
towerofhanoi(num, 'A', 'C', 'B')
