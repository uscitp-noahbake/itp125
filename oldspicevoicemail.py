import os, sys, time
import argparse
import urllib2
# website containing relevant files
web  = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/"
# make voicemail into vectors
fem_begin = ["f-b1-hello_caller.mp3","f-b2-lady_at.mp3"]
male_begin = ["m-b1-hello.mp3","m-b2-have_dialed.mp3"]
fem_req= ["f-r0.1-unable_to_take_call.mp3","f-r0.2-she_is_busy.mp3"]
male_req = ["m-r0-cannot_come_to_phone.mp3","m-leave_a_message.mp3"]
fem_reasons = ["f-r1-ingesting_old_spice.mp3","f-r2-listening_to_reading.mp3","f-r3-lobster_dinner.mp3","f-r4-moon_kiss.mp3","f-r5-riding_a_horse.mp3"]
male_reasons = ["m-r1-building.mp3","m-r2-cracking_walnuts.mp3","m-r3-polishing_monocole.mp3","m-r4-ripping_weights.mp3"]
fem_endings = ["f-e1-she_will_get_back_to_you.mp3","f-e2-thanks_for_calling.mp3"]
male_endings = ["m-e1-horse.mp3","m-e2-jingle.mp3","m-e3-on_phone.mp3","m-e4-swan_dive.mp3","m-e5-voicemail.mp3"]



# argparse arguments
if __name__ == "__main__":
    # makes command lines avaliable to user
    parser = argparse.ArgumentParser( description = 'Input all the variable for voicemail')
    # each argument added are the ones that will be asked in the program
    parser.add_argument('-g', help = 'Gender', type = str)
    parser.add_argument('-n', help = 'Number', type = int)
    parser.add_argument('-r', help = 'Reason', type = int)
    parser.add_argument('-e', help = 'Ending', type = int)
    parser.add_argument('-o', help = 'Output', type = str)
    args = parser.parse_args()
# Overarching while loop in case user wishes to c settings
while True:
    # Main program
    # Setup output file for testing
    output_file = open("test.mp3","wb")
    # Open a txt file containing the mp3 files the user chose
    output_file2 = open("mp3files.txt","w")

    gender_selected = False
    # Satisfy argparse
    if args.g is not None:
        gender_selected = True
        gender_input = args.g
    # male or female?
    while not gender_selected:
        gender_input = raw_input("Please enter m or f for male or female then press enter: ")
        if gender_input in('m', 'f'):
            # jump out of while loop
            gender_selected = True
        else:
            print 'Input Invalid.'

    # download 0.mp3 from website
    # if chosen gender female
    if gender_input is 'f':
        
        response = urllib2.urlopen(web + fem_begin[0])
        output_file.write(response.read())
        # mp3 file + txt file
        response2 = (web + fem_begin[0])
        output_file2.write(response2 + "\n")

        response = urllib2.urlopen(web + fem_begin[1])
        output_file.write(response.read())
        response2 = (web + fem_begin[1])
        output_file2.write(response2 + "\n")

    # if chosen gender male
    if gender_input is 'm':
        
        response = urllib2.urlopen(web + male_begin[0])
        output_file.write(response.read())
        # The other file storing info after user made a choice
        response2 = (web + male_begin[0])
        output_file2.write(response2 + "\n")

        response = urllib2.urlopen(web + male_begin[1])
        output_file.write(response.read())
        response2 = (web + male_begin[1])
        output_file2.write(response2 + "\n")

    # User phone number
    count = 0
    phone_selected = False
    # check qualifications, restart if not satisfied
    while not phone_selected:
        clean_phone_input = ""
        if args.n is not None:
            phone_input = str(args.n)
            phone_selected = True
        else:
            phone_input = raw_input("Enter phone number: ")
            count = 0
        for character in phone_input:
            # check input digits
            if character.isdigit():
                clean_phone_input += character
                count = count + 1
        if count == 10:
            phone_selected = True


    for digit in clean_phone_input:
        #download mp3 from website
        response = urllib2.urlopen(web + digit + '.mp3')
        #write file
        output_file.write(response.read())
        response2 = (web + digit + '.mp3')
        output_file2.write(response2 + "\n")

    # Need to set up reasons based on gender.
    if gender_input is 'f':
        response = urllib2.urlopen(web + fem_req[0])
        output_file.write(response.read())
        response2 = (web + fem_req[0])
        output_file2.write(response2 + "\n")

        response = urllib2.urlopen(web + fem_req[1])
        output_file.write(response.read())
        response2 = (web + fem_req[1])
        output_file2.write(response2 + "\n")
        # while loop for reasons
        reason_input = ""
        if args.r is not None:
            reason_input = args.r
        else:
            # problems with condition so must change input to int so it compares with other int
            while not ( len(str(reason_input)) == 1 and int(reason_input) > 0 and int(reason_input) <= 5 ):
                reason_input = ""
                print '[1] ...ingesting my delicious old spice man smell.\n[2] ...listening to me read romantic poetry while I make a bouquet of paper flowers from each red page.\n[3] ...enjoying a delicious lobster dinner I prepared just for her, while carrying her on my back safely through piranha infested waters.\n[4] ...being serenaded on the moon with a view of the earth while surviving off the oxygen in my lungs via passionate kiss.\n[5] ...riding a horse backwards with me.\n'
                reason_user_input = raw_input("Enter the reason you aren't available (numbers 1-5):")
                # other method to change string, otherwise int does not work
                try:
                    reason_input = int(reason_user_input)
                # checks for int, otherwise while loop starts over
                except ValueError:
                    print "Invalid input!"

        response = urllib2.urlopen(web + fem_reasons[int(reason_input)-1])
        output_file.write(response.read())
        response2 = (web + fem_reasons[int(reason_input)-1])
        output_file2.write(response2 + "\n")

        # only one ending choice
        # same concept with reason
        ending_input = ""
        if args.e is not None:
            reason_input = args.e
        else:
            while not (len(str(ending_input)) == 1 and int(ending_input) > 0 and int(ending_input) <= 2 ):
                ending_input = ""
                print '[1] ...but she\'ll get back to you as soon as she can.\n[2] Thanks for calling.\n'
                ending_user_input = raw_input("Enter the ending you want in your voicemail (numbers 1 or 2):")
                try:
                    ending_input = int(ending_user_input)
                except ValueError:
                    print "Invalid input!"

        response = urllib2.urlopen(web + fem_endings[int(ending_input)-1])
        output_file.write(response.read())
        response2 = (web + fem_endings[int(ending_input)-1])
        output_file2.write(response2 + "\n")

    if gender_input is 'm':
        response = urllib2.urlopen(web + male_req[0])
        output_file.write(response.read())
        response2 = (web + male_req[0])
        output_file2.write(response2 + "\n")

        reason_input = ""
        if args.r is not None:
            reason_input = args.r
        else:
            while not ( len(str(reason_input)) == 1 and int(reason_input) > 0 and int(reason_input) <= 4 ):
                reason_input = ""
                print '[1] ...they\'re building an orphanage for children with their bare hands while playing a sweet, sweet lullaby for those children with two mallets against their ab xylophone.\n[2] ...cracking walnuts with their man mind.\n[3] ...polishing their monocle smile.\n[4] ...ripping out mass loads of weights\n'
                reason_user_input = raw_input("Enter the reason you want in your voicemail (numbers 1-4):")
                try:
                    reason_input = int(reason_user_input)
                except ValueError:
                    print "Invalid input!"

        response = urllib2.urlopen(web + male_reasons[int(reason_input)-1])
        output_file.write(response.read())
        response2 = (web + male_reasons[int(reason_input)-1])
        output_file2.write(response2 + "\n")
        # voicemail + reason
        response = urllib2.urlopen(web + male_req[1])
        output_file.write(response.read())
        response2 = (web + male_req[1])
        output_file2.write(response2 + "\n")

        ending_input = ""
        if args.e is not None:
            ending_input = args.e
        else:
            while not (len(str(ending_input)) == 1 and int(ending_input) > 0 and int(ending_input) <= 5 ):
                ending_input = ""
                print '[1] ...I\'m on a horse.\n[2] ...doo. doo. dooooo doo.. doo.. doo.doo.doo\n[3] ...I\'m on a phone.\n[4] ...swan dive\n[5] ...This voicemail is now diamonds.\n'
                ending_user_input = raw_input("Enter the ending you want in your voicemail (numbers 1-5):")
                try:
                    ending_input = int(ending_user_input)
                except ValueError:
                    print "Invalid input!"

        response = urllib2.urlopen(web + male_endings[int(ending_input)-1])
        output_file.write(response.read())
        response2 = (web + male_endings[int(ending_input)-1])
        output_file2.write(response2 + "\n")

    if args.g is not None and args.n is not None and args.r is not None and args.e is not None and args.o is not None:
        old_name = "test.mp3"
        new_name = str(args.o)

        output_file.close()
        os.rename(old_name, new_name + ".mp3")
        output_file2.close()
        break
    else:
        # Let user's know their settings
        print "Your setting is:\nGender: %s\nPhone Number: %s\nReason #%d\nEnding #%d" % (gender_input, phone_input,reason_input, ending_input)

        setting_selected = False
        while not setting_selected:
            setting_input = raw_input("Confirm settings (y,n)? ")
            if setting_input in('y', 'n'):
                setting_selected = True
            else:
                print 'Invalid input.'
        if setting_input is 'y':
            old_name = "test.mp3"
            # close file
            output_file.close()
            # rename file with new name
            new_name = raw_input("Name your file: ")
            os.rename(old_name, new_name + ".mp3")
            output_file2.close()
            break

        if setting_input is 'n':
            # closing files
            output_file.close()
            output_file2.close()
            # closing file then remove content
            os.remove(output_file.name)
            os.remove(output_file2.name)
            # Restart overarching while loop
            False
