Title: Code Syntax Test
Date: 2017-08-17 15:59
Category: Code
Status: draft

This is a test of code syntax

This is a bash script:
```
#!/bin/bash 

ERROR_FILE=$(mktemp -p $HOME/tmp ssh_wrapper.XXXXXXXX)
USER_KNOWN_HOST_FILE=$HOME/.ssh/known_hosts

ssh $* 2> $ERROR_FILE 

if [ $? -ne 0 ] 
then
  cat $ERROR_FILE
  echo "SSH returned an error!"
  if egrep '^Offending key in' $ERROR_FILE > /dev/null
  then
    KNOWN_HOSTS_FILE_WLINE=$(egrep '^Offending key in' $ERROR_FILE | awk '{sub(/\r/,"",$4); print $4}')
    KNOWN_HOSTS_FILE_WLINE=${KNOWN_HOSTS_FILE_WLINE%\r}
    KNOWN_HOSTS_FILE=$(echo $KNOWN_HOSTS_FILE_WLINE | awk -F':' '{print $1}')
    OFFENDING_KEY_LINE=$(echo $KNOWN_HOSTS_FILE_WLINE | awk -F':' '{print $2}')
    if [ $KNOWN_HOSTS_FILE == '/etc/ssh/ssh_known_hosts' ]
    then
      echo -n "Run config management to get new key? (y/[N])? "   
      read CHOICE
      if [ "x$CHOICE" == "xy" ]
      then
        sudo bcfg2 -qv 
      else
        echo -n "Use ssh-keyscan to put new key in your user's knownhost config? (y/[N])? "       
        read CHOICE
        if [ "x$CHOICE" == "xy" ]
        then
          NEW_KEY=$(ssh-keyscan $*) 
          if [ $? -eq 0 ]
          then
            echo $NEW_KEY >> $USER_KNOWN_HOST_FILE
          else 
            echo "\"ssh-keyscan $*\" failed, Try re-runing this script with just the hostname as the only argument"
          fi
        fi
      fi
    else
      echo -n "Remove offending key (y/[N])? "    
      read CHOICE
      if [ "x$CHOICE" == "xy" ]
      then
        sed -i "${OFFENDING_KEY_LINE}d" $KNOWN_HOSTS_FILE
      fi
    fi
  fi
fi
```
