#You have an array of logs. Each log is space delimited string of words.
#For each log, the first word ing each log is an alphanumeric identifier
#Each word after the identifier will consist only of lowercase letters, or
#Each word after the identifier will consist only of digits

Input_logs = ["dig1 8 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
letters, digits = [], []

class Solution:
    def reorderLogFiles(self, logs):
        for log in Input_logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

Output_logs = Solution()

print(Output_logs.reorderLogFiles(Input_logs))
