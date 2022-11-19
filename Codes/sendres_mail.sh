#!/bin/bash
echo "Very sad life"
FILE1=$1
python3 send_res_DT.py >saveit.txt
sendmail -t $FILE1 -t <saveit.txt

# instraction to run the file
# ./sendres_mail.sh username@domain.com
# will send the HR to the user data
