import json
import matplotlib.pyplot as plt

RELIABLE_RANGE = (1000, 5000)

problems = json.load(open(f'data/json/problems.json'))['result']
print("There are a total of ", len(
    problems['problems']), "problems on the platform")  # problemStatistics

print(problems['problems'][0])
print(problems['problemStatistics'][0])  # only solvedCount is extra

problemStats = problems['problemStatistics']
problems = problems['problems']
problemRatings = []
solvedCounts = []


print("Reliable range :", RELIABLE_RANGE)

reliableSubmissions = 0
reliableProblems = 0
tagCounter = {}
for i, problem in enumerate(problems):
    if 'rating' in problem:
        problemRatings.append(problem['rating'])
    if 'solvedCount' in problemStats[i] and problemStats[i]['solvedCount'] > RELIABLE_RANGE[0] and problemStats[i]['solvedCount'] < RELIABLE_RANGE[1]:
        reliableSubmissions += problemStats[i]['solvedCount']
        reliableProblems += 1
        solvedCounts.append(problemStats[i]['solvedCount'])
        problemTags = problem['tags']
        for tag in problemTags:
            if tag in tagCounter:
                tagCounter[tag] += 1
            else:
                tagCounter[tag] = 1

plt.hist(problemRatings, bins=100)
plt.show()

plt.hist(solvedCounts, bins=50)
plt.show()


plt.bar(range(len(solvedCounts)), solvedCounts)
plt.show()


print("number of reliable submissions : ", reliableSubmissions)
print("number of reliable problems : ", reliableProblems)

print("unique Tags : ", tagCounter)
