    echo "$(tput setaf 2)
       .~~.   .~~.    `date +"%A, %e %B %Y, %R"`
      '. \ ' ' / .'   `uname -srmo`$(tput setaf 1)
       .~ .~~~..~.   
      : .~.'~'.~. :   
     ~ (   ) (   ) ~  CPU................: `top -n1 | awk '/Cpu\(s\):/ {print $2}'` % 
    ( : '~'.~.'~' : ) Memory.............: `cat /proc/meminfo | grep MemFree | awk {'print $2'}`kB (Free) / `cat /proc/meminfo | grep MemTotal | awk {'print $2'}`kB (Total)
     ~ .~ (   ) ~. ~  Running Processes..: `ps ax | wc -l | tr -d " "`
      (  : '~' :  )   
       '~ .~~~. ~'    
           '~'
    $(tput sgr0)"
