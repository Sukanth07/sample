class mark:
    def __init__(self):

        self.marks10=[]
        self.subject10=["Tamil","English","Maths","Science","Social"]

        self.marks11=[]
        self.avg_marks11=[]
        self.subject11=["Language","English","Physics","Chemistry","Computer","Maths"]

        self.marks12=[]
        self.subject12=["Language","English","Physics","Chemistry","Computer","Maths"]

    def round_off(self,w):
        self.w=w
        self.w1=float(self.w)
        self.w2=int(self.w)
        self.w3=self.w1-self.w2
        if self.w3>=0.5:
            return self.w2+1
        else:
            return self.w2

    def get_marks10(self):
        print("\n--------------------------------10th Mark--------------------------------\n")
        print("Enter Your 10th Marks:-")
        print("``````````````````````")
        self.x=":"
        for i in range(len(self.subject10)):
            self.y=(f'{self.subject10[i]:12}{self.x}')
            print(self.y,end="")
            a=int(input())
            self.marks10.append(a)

    def show_top3(self):
        print("\nYour Highest Three Marks:-")
        print("````````````````````````")
        self.d10={self.subject10[i]:self.marks10[i] for i in range(len(self.subject10))}
        self.dd10=dict(sorted(self.d10.items(),key=lambda k:k[1],reverse=True))
        self.l1=list(self.dd10.keys())
        self.l2=list(self.dd10.values())
        self.x=":"
        self.sum1=0
        for i in range(0,3):
            self.y=(f'{self.l1[i]:12}{self.x}')
            print(self.y,self.l2[i])
            self.sum1=self.sum1+self.l2[i]
            #print(type(self.l2[i]))

        self.av=float((self.sum1/300)*50)
        print("\nYour 10th 50% Mark With Highest Three Subjects :",self.round_off(self.av))
        #self.av1=float(self.av)
        #self.av2=int(self.av)
        #self.av3=self.av1-self.av2
        #if self.av3>=0.5:
            #self.av2+=1
            #print("\nYour 10th 50% Mark With Highest Three Subjects :",self.av2)
        #else:
            #print("\nYour 10th 50% Mark With Highest Three Subjects :",self.av2)
        
    def get_marks11(self):
        print("\n--------------------------------11th Mark--------------------------------\n")
        print("Enter Your 11th Marks (Only Theory):-")
        print("```````````````````````````````````")
        self.x=":"
        for i in range(len(self.subject11)):
            self.y=(f'{self.subject11[i]:12}{self.x}')
            print(self.y,end="")
            self.a=int(input())
            self.marks11.append(self.a)

    def show_avg_marks11(self):
        print("\nThe 20% Of Your 11th Marks (Only Theory):-")
        print("````````````````````````````````````````")

        for i in range(0,2):   #for language, english subjects
            self.a=float((self.marks11[i]/90)*20)
            self.a1=int(self.a)
            self.a2=self.a-self.a1
            if self.a2>=0.5:
                self.a1+=1
                self.avg_marks11.append(self.a1)
            else:
                self.avg_marks11.append(self.a1)

        for i in range(2,5):   #for physics, chemistry, computer subjects
            self.a=float((self.marks11[i]/70)*20)
            self.a1=int(self.a)
            self.a2=self.a-self.a1
            if self.a2>=0.5:
                self.a1+=1
                self.avg_marks11.append(self.a1)
            else:
                self.avg_marks11.append(self.a1)

        for i in range(len(self.marks11)):   #for maths subject
            if i<(len(self.marks11)-1):
                continue
            else:
                self.a=float((self.marks11[i]/90)*20)
                self.a1=int(self.a)
                self.a2=self.a-self.a1
                if self.a2>=0.5:
                    self.a1+=1
                    self.avg_marks11.append(self.a1)
                else:
                    self.avg_marks11.append(self.a1)
        self.x=":"
        for i in range(len(self.subject11)):
            self.y=(f'{self.subject11[i]:12}{self.x}')
            print(self.y,self.avg_marks11[i])

    def show_marks12(self):
        print("\n--------------------------------12th Mark--------------------------------\n")
        self.practical=30
        print("Your 12th Internal & Practical Mark Together :",self.practical)
        print("\nYour 12th Marks:-")
        print("```````````````")
        self.x=":"
        self.total=0
        for i in range(len(self.subject12)):
            self.t=self.av2+self.avg_marks11[i]+self.practical
            self.y=(f'{self.subject12[i]:12}{self.x}')
            print(self.y,self.t)
            self.marks12.append(self.t)
            self.total=self.total+self.t
            self.t=0

    def endcard(self):

        print("\nYour 12th Total Mark Out Of 600 :",self.total)

        self.per=float((self.total/600)*100)
        self.per1=int(self.per)
        self.per2=self.per-self.per1
        if self.per2>=0.5:
            self.per1+=1
            print("\nPercentage Of Your 12th Mark :",self.per1,"%")
        else:
            print("\nPercentage Of Your 12th Mark :",self.per1,"%")
        
        self.cutoff=(self.marks12[2]/2)+(self.marks12[3]/2)+self.marks12[5]
        print("\nYour 12th CutOff Mark (Physics,Chemistry,Maths) :",self.cutoff)
                      
        
    def display(self):
        self.get_marks10()
        self.show_top3()
        self.get_marks11()
        self.show_avg_marks11()
        self.show_marks12()
        self.endcard()


stud=input("\nEnter Student Name : ")
o=mark()
o.display()

#Fuck