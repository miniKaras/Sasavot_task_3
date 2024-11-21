import heapq
import random as rnd
import time
import matplotlib.pyplot as plt


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, n, p):
        heapq.heappush(self.heap, (-p, n))

    def extract_max(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[1]


class Node:
    def __init__(self, n, p):
        self.value = n
        self.priority = p
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, n, p):
        new_node = Node(n, p)
        if self.head is None or self.head.priority < p:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next is not None) and (current.next.priority >= p):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def extract_max(self):
        if self.head is None:
            return None
        max_element = self.head.value
        self.head = self.head.next
        return max_element


# def insert_time_measurement(a):
#     start_time = time.perf_counter()
#     a.insert(1, 1)
#     end_time = time.perf_counter()
#     return end_time - start_time


# def extract_time_measurement(a):
#     start_time = time.perf_counter()
#     a.extract_max()
#     end_time = time.perf_counter()
#     return end_time - start_time


x = [_ for _ in range(1000, 5001, 1000)]
binary_heap_inserts_avg = []
binary_heap_extracts_avg = []
linked_list_inserts_avg = []
linked_list_extracts_avg = []
for n in x:
    array_of_values = [rnd.randint(1, 1000) for _ in range(n)]
    priority_array = rnd.sample(range(1, n + 1), n)

    binary_heap = BinaryHeap()
    linked_list = LinkedList()

    for i, j in zip(array_of_values, priority_array):
        binary_heap.insert(i, j)

    for i, j in zip(array_of_values, priority_array):
        linked_list.insert(i, j)

    binary_heap_inserts = []
    binary_heap_extracts = []
    linked_list_inserts = []
    linked_list_extracts = []
    for i in range(1000):
        start_time = time.perf_counter()
        binary_heap.insert(rnd.randint(1,1000), rnd.randint(1,n))
        end_time = time.perf_counter()
        binary_heap_inserts.append( end_time - start_time)

        start_time = time.perf_counter()
        linked_list.insert(rnd.randint(1,1000), rnd.randint(1,n))
        end_time = time.perf_counter()
        linked_list_inserts.append(end_time - start_time)

        start_time = time.perf_counter()
        binary_heap.extract_max()
        end_time = time.perf_counter()
        binary_heap_extracts.append(end_time - start_time)

        start_time = time.perf_counter()
        linked_list.extract_max()
        end_time = time.perf_counter()
        linked_list_extracts.append(end_time - start_time)
    binary_heap_inserts_avg.append(sum(binary_heap_inserts)/1000)
    binary_heap_extracts_avg.append(sum(binary_heap_extracts) / 1000)
    linked_list_extracts_avg.append(sum(linked_list_extracts) / 1000)
    linked_list_inserts_avg.append(sum(linked_list_inserts) / 100)

    # binary_heap_inserts.append(insert_time_measurement(binary_heap))
    # linked_list_inserts.append(insert_time_measurement(linked_list))
    #
    # binary_heap_extracts.append(extract_time_measurement(binary_heap))
    # linked_list_extracts.append(extract_time_measurement(linked_list))

fig, axs = plt.subplots(2, figsize=(8, 6))

axs[0].plot(x, binary_heap_inserts_avg, label="бинарная вставка", color="blue")
axs[0].plot(x, linked_list_inserts_avg, label="вставка листа", color="orange")
axs[0].legend()
axs[0].set_title("вставка")

axs[1].plot(x, binary_heap_extracts_avg,  label="бинарное доставание", color="green")
axs[1].plot(x, linked_list_extracts_avg, label="листовое доставание", color="red")
axs[1].legend()
axs[1].set_title("доставание")


plt.tight_layout()
plt.show()
