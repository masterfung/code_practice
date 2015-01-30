list_of_numbers = [2.4,9,18,29,2,4,5,9]

def median(array):
	sort_list = sorted(array)
	if len(sort_list) % 2 == 1:
		median_num = int(round(len(sort_list)/2.0))
		return median_num
	else:
		middle = len(sort_list) / 2
		median_num = (sort_list[middle-1] + sort_list[middle]) / 2
		return median_num

print median(list_of_numbers)


def mean(array):
	sum = 0
	for x in array:
		sum += x
	return sum / len(array)

print mean(list_of_numbers)