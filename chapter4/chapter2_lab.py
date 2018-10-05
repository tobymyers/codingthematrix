# file = open('US_senate_voting_data_109.txt')
# mylist =[(line.split(' ')) for line in file]
# print(mylist)
#2.12.1
def create_voting_dict(strlist):
    dic = {string[0]:string[3:-1] for string in strlist}
    for key, val in dic.items():
        ints = [int(str) for str in val]
        dic[key] = ints
    return dic
voting_dict = create_voting_dict(mylist)
print(voting_dict)
#2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    assert sen_a in voting_dict and sen_b in voting_dict
    return sum([a*b for a,b in zip(voting_dict[sen_a], voting_dict[sen_b])])
print(policy_compare('Warner', 'Wyden', voting_dict))

#2.12.3
def most_similar(sen, voting_dict):
    return max([(policy_compare(sen, sen_i, voting_dict),sen_i) for sen_i in voting_dict if sen_i != sen])
#2.12.4
def least_similar(sen, voting_dict):
    return min([(policy_compare(sen, sen_i, voting_dict),sen_i) for sen_i in voting_dict if sen_i != sen])

#2.12.5
print(least_similar('Santorum', voting_dict)) #Feingold, 4
print(most_similar('Chafee', voting_dict))  #Jeffords, 39

#2.12.6
print(policy_compare('Obama', 'Boxer', voting_dict))
#31, pretty similar

#2.12.7
#compute average dot product for each senator in sen_set dot sen
def find_average_similarity(sen, sen_set, voting_dict):
    dot = []
    for senator in sen_set:
        dot.append(policy_compare(sen, senator, voting_dict))
    return (round(sum(dot)/len(dot),2), sen)

dem_list = [line[0] for line in mylist if line[1]=='D']
def find_most_similar(dem_list, voting_dict):
    similarity = []
    for sen in voting_dict.keys():
        similarity.append(find_average_similarity(sen, dem_list, voting_dict))
    return max(similarity)
print(find_most_similar(dem_list, voting_dict))

#2.12.8
summ = [0] * len(voting_dict['Feinstein'])
for sen, record in voting_dict.items():
    if sen in dem_list:
        for i in range(len(record)):
            summ[i] += record[i]

result = []
avg = [round(i/(len(summ)),1) for i in summ] #seems like there should be negative nums here
for sen, record in voting_dict.items():
    dot = sum([avg[i]*record[i] for i in range(len(summ))])
    result.append((dot, sen))
print(max(result)) #Biden again!!  Different b/c of rounding errors

#2.12.9
def bitter_rivals(original_voting_dict):
    voting_dict = dict(original_voting_dict)
    rivals = set()
    for sen, record in voting_dict.items():
        for sen2, record2 in voting_dict.items():
            rivals.add((policy_compare(sen, sen2, voting_dict), sen, sen2))
    return min(rivals)
print(bitter_rivals(voting_dict),'<<most bitter rivals, but still only disagree a tiny bit more than they agree')

print(policy_compare('Obama', 'McCain', voting_dict),'Obama/McCain')
