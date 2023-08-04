"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
        nums = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        numsdigit = ["oh", " ", "twenty", "thirty", "forty", "fifty"]
        pm = False
        first = int(input_time[:2])
        last = (input_time[3:])
        if first > 12:
            first = first - 12
            pm = True
        str = "It's " + nums[first] + " "
            
        if last == "0":
            pass
        else:
            str += numsdigit[int((last)[0])] + " "
            str += nums[int((last)[1])]
        if pm:
            str += " " + "pm"
        else:
            str += " " + "am"
        print(str)
        return str
            #type input_time: string
            #return type: string
            
            #TODO: Write code below to return a string with the solution to the prompt.
            

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        
