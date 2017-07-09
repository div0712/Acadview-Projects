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

            def send_a_message(spy_name):
                global count
                position = select_a_friend(
                    spy_name)
                if position == "null":
                    return (0)
                else:
                    f_name = spy_detail[spy_name]["friends"].keys()[position]
                    from steganography.steganography import Steganography
                    i_path = "C:\Users\Divyesh\PycharmProjects\ACADVIEW\\"
                    i_img_name = raw_input("What is the image name(Type along with the extension)?: ")
                    path = i_path + i_img_name
                    print "your path with specified image name is: " + path
                    o_img_name = raw_input("What name should be the output file?(Type along with extension): ")
                    o_path = "C:\Users\Divyesh\PycharmProjects\ACADVIEW\\"
                    output_path = o_path + o_img_name
                    text = raw_input("Enter the TEXT you want to encode: ")
                    from datetime import datetime
                    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    count = count + 1
                    spy_detail[spy_name]["friends"][f_name]["chat"].update({count: {"text": text, "time": date,
                                                                                    "boolean": True}})
                    print "please wait..................................."
                    s = text.strip().split(" ")
                    Steganography.encode(path, output_path, text)
                    print "\nMessage has been encoded and sent to %s.\n" % (
                    str(spy_detail[spy_name]["friends"].keys()[position]))
                    for i in range(len(s)):
                        for j in range(len(special_words)):
                            if special_words[j] == s[i]:
                                print "Your message was an emergency message.\n"
                    if len(text) > 100:
                        del spy_detail[spy_name]
                        print "%s has been deleted from dictionary for speaking more than 100 words. Kindly create account again. :)" % (
                        spy_name)
                        return (1)
                    else:
                        return (0)