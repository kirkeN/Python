import json
def total_score(scores):
	sum = 0
	s_dict = json.loads(scores)
	for item in s_dict:
		sum += s_dict[item]
	return json.dumps({"total_score": sum})

#print(total_score('{"john": 10, "steve": 31}'))
		

