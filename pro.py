spy_detail={}
spy_history={}
status=[]
count=0

def addstatus(spy_name):
    loop=0
    if spy_detail[spy_name]["status"]== "":
        print "You are not having previous status\n"
        loop=1
        if loop==0:
            print "You are havi2ng predefined status which is : "+str(spy_detail[spy_name]["status"])
        choice=int(raw_input("STATUS OPTIONS :1.Choose from predefined list of status\n2.Choose from your status hisory\n3.Create new status\nPress 1 or 2 or 3: "))
        if choice==1:
            length=len(status)
            for i in range(0, length):
                print "%s. " % (i + 1) + status[i]
            status_1 = int(raw_input("Enter the number corresponding to status you want to choose: "))
            spy_detail[spy_name]["status"] = status[status_1 - 1]
            if spy_detail[spy_name]["status"] not in spy_status_history[spy_name]:
                spy_status_history[spy_name].append(
                    spy_detail[spy_name]["status"])
            print "\nStatus uploaded successfully"
            print "Your status is : " + str(spy_detail[spy_name]["status"])
        elif choice == 2:  # for status history
            length = len(spy_status_history[spy_name])
            if length == 0:
                print "\nYou have no previous status.\n"
            else:
                for i in range(0, length):
                    print "%s. " % (i + 1) + spy_status_history[spy_name][i]
                status_1 = int(raw_input("Enter the number corresponding to status you want to choose: "))
                spy_detail[spy_name]["status"] = spy_status_history[spy_name][
                    status_1 - 1]
                print "\nStatus uploaded successfully"
                print "Your status is : " + str(spy_detail[spy_name]["status"])
        elif choice == 3:
            status_1 = raw_input("Enter your new status: ")
            spy_detail[spy_name]["status"] = status_1
            print "\nStatus uploaded successfully"
            print "Your status is : " + str(spy_detail[spy_name]["status"])
            spy_status_history[spy_name].append(status_1)
            if spy_detail[spy_name]["status"] not in spy_status_history[spy_name]:
                spy_status_history[spy_name].append(
                    spy_detail[spy_name]["status"])
        else:
            print "\nWrong input, Try again"
        return ()

    def add_friend(spy_name):
        f_name = raw_input("Enter your friend's name: ")
        if len(f_name) == 0:
            print "Name cannot be empty. Try again.\n"
            return (0)
        f_age = int(raw_input("Enter your friend's age: "))
        if f_age < 12 or f_age > 50:
            print "Sorry cannot add friend. Cannot authenticate the age.\n"
            return (0)
        f_rating = float(raw_input("Enter your friend's rating: "))
        if f_rating < spy_detail[spy_name]["rating"]:
            print "Sorry cannot add friend. Rating not more than yours.\n"
            return (0)
        spy_detail[spy_name]["friends"].update({f_name: {"f_age": f_age, "f_rating": f_rating,"chat": {}}})
        print "\nFriend has been added successfully.\n Details of the recently added friend:\n%s \n" % (f_name) + str(
            spy_detail[spy_name]["friends"][f_name])
        return (len(spy_detail[spy_name]["friends"].keys()))

    def select_a_friend(spy_name):
        leng = len(spy_detail[spy_name]["friends"])
        if leng == 0:
            print "You have no friends added. \n"
            return ("null")
        else:
            print "You have following people in your friend list: \n"
            for i in range(0, leng):
                print str(i + 1) + ". " + str(spy_detail[spy_name]["friends"].keys()[i])
            position = int(
                raw_input("Enter the number corresponding to your choice of friend with whom you want to continue: "))
            position = position - 1
            if (position < 0 or position >= leng):
                print "You have entered a wrong input\nTry again.\n"
                return ("null")
            else:
                return (position)