target = []
target = [0, 1, 2, 3, 4, 5]
target2 = [1, 2, "hello", ["what", 1, (23, 45, "t")]]
the_list = list(range(10)))
the_list=list({"only": 0, "keys": 1, "will": 2, "become": 3, "elements"}))

new_list=old_list_a + old_list_b

target[3]="three"
target2[3][0]="where"


target=["the", "new", "content", "to", "replace", "the", "old", "one"]
target.append("another element")


target.remove("only the first instance")


del(target[0])
target.insert(0, "first element")

evaluation=(3 in target)
evaluation=(3 not in target)

target.extend(range(5))
target.extend(target2)
target.extend(("a", "b", "c"))


target.insert(5, "inserted element,other's move back")


listb.count("how many of this element")
listb.index("index of the first occurrance")


outlast=["pop out the last element"].pop()
outfirst=target4.pop(0)
outindex=target4.pop(3)





# using list as a stack, first one in first one out

target3=[1, 2, 3, 4]
# it push out the last element of target3, and assign it to a
a=target3.pop()
print("list as stack", target3, f"a={a}")

# using list as a deque, first one in last one out

from collections import deque                # import deque module
target3=[1, 2, 3, 4]
queue=deque(target3)                        # create deque object
# it push out the first element of queue,and assign it to a
a=queue.popleft()
print("list as deque", queue, f"a={a}")
