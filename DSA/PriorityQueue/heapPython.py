import heapq
# priority_queue = []
# heapq.heappush(priority_queue, (3, "Task A"))
# heapq.heappush(priority_queue, (1, "Task B"))
# heapq.heappush(priority_queue, (2, "Task C"))
# print(priority_queue)
# highest_priority_task = heapq.heappop(priority_queue)
# print(highest_priority_task)
# print(priority_queue)

# task_list = [(3, "Task A"), (1, "Task B"), (2, "Task C")]
# heapq.heapify(task_list)
# print(task_list)

number_list = [3,1,5,2,4]
print(number_list)

negative_number_list = [-number for number in number_list]
print(negative_number_list)

heapq.heapify(number_list)
print(number_list)

heapq.heapify(negative_number_list)
print(negative_number_list)
