# Add the following lines to maven.sh
export TZ="America/New_York"
export EDITOR=vim
export M2_HOME=/opt/apache-maven-3.0.5
export M2=$M2_HOME/bin
export PATH=$M2:$PATH 
export a b c d e f g h i j k l m n o p q r s t u v w x y z
export NODE_PATH="~/node_modules"
export CDPATH=".:~"
export GOROOT="$HOME/go"
export PATH=~/bin:/bin:/usr/bin:/usr/local/bin:$GOROOT/bin:/opt/local/bin:/opt/local/sbin:$PATH
export LC_COLLATE=C
export GREP_OPTIONS='--color=auto'
export GOROOT="/usr/local/go"
HISTSIZE=10000000
SAVEHIST=10000000

# some aliases
#alias sfe="sudo srm -zsv"

alias z="vi ~/.zshrc;. ~/.zshrc"
alias firefox="/Applications/Firefox.app/Contents/MacOS/firefox"
alias _="cd $_"
alias rserv="ruby -run -e httpd . -p"
alias ste="sudo srm -rmv ~/.Trash"
alias sfe="sudo diskutil secureErase freespace 0"
alias n="~/weather-station/launch.sh"
alias vv="vi svg_sun_up.svg sunrise_parse.py template.svg parse_weather.py"
alias chrome="'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' --headless --disable-gpu --screenshot=moon.png moon.html"
alias ws="cd /Users/jamestjordan/weather-display/server; nohup python -m SimpleHTTPServer 8000 &" 
alias dcn="sudo docker ps -notrunc"
alias lxa="sudo lxc-attach -n"
alias lh="history | less -n"
alias pst="ps afx"
alias dri='sudo docker rmi $( sudo docker images | grep "^<none>" | awk "{print $3}")'
alias dr="sudo docker run -t -d -P -name "
alias dsh="sudo docker run -a stdin -a stdout -i -t ubuntu /bin/bash"

alias drm="sudo docker rm"
alias drmi="sudo docker rmi"
alias da="sudo docker attach"
alias dp="sudo docker port"
alias dc="sudo docker ps"
alias di="sudo docker images"
alias dh="sudo docker help"
alias dhst="sudo docker history"
alias dt="sudo docker top"
alias dhs="sudo docker history"
alias dv="sudo docker version"
alias d0="sudo docker stop"
alias d1="sudo docker start"
alias vd="vi Dockerfile"
alias d="sudo docker"
alias vc="sudo vi ~/projects/MyProject/conf/trac.ini"
alias server="python -m SimpleHTTPServer"
alias sai="sudo apt-get install"
alias lip="curl http://169.254.169.254/latest/meta-data/local-ipv4;echo"
alias a=type
alias ch="sudo chef-server-ctl"
alias ff="sudo find / -name"
alias wp="sudo netstat -tulpn>/tmp/wp.$$; sudo ps -ef>>/tmp/wp.$$;less -n /tmp/wp.$$;rm /tmp/wp.$$"
alias lnm="ls ~/node_modules"
alias plan="vi ~/.plan;"
alias cj='cat *.json'
alias lj='less *.json'
alias g=git
alias gp="git pull"
alias gco="git checkout"
alias gr="git reset --hard HEAD"
alias ga="git add"
alias gpt="git push origin --tags"
alias gts="git tag"
alias gc="git commit -a -m '`date`';gpom"
alias gs="git status"
alias gpom="git push origin master"
alias sg="sudo su git"
alias myip='echo `curl -s http://169.254.169.254/latest/meta-data/public-ipv4`'
alias ua=unalias
alias us=unset
alias c8="cd *"
alias v8="vim *"
alias n8="node *.js"
alias l8="less *"
alias vi=vim
alias y='cat *.yml'
alias -- -="cd -;"
alias sx="svn ci -mz"
alias vf="vim ~/.filterwords"
alias p.="p=\`pwd\`"
alias cd.='cd $_;l'
alias ccd="cdd"
alias cl="clear"
alias c="ccd"
alias ..="cd ..;"
alias ...="cd ../..;"
alias ....="cd ../../..;"
alias crc="./cruisecontrol.sh"
alias cs=csvn
alias e="cd ~;vi .vimrc;cd -"
alias h='history'
alias j=jobs
alias k1="kill -9 %1"
alias k2="kill -9 %2"
alias k3="kill -9 %3"
alias k4="kill -9 %4"
alias k5="kill -9 %5"
alias k6="kill -9 %6"
alias k7="kill -9 %7"
alias k8="kill -9 %8"
alias k9="sudo kill -9"
alias la='ls -A'
alias ll='ls -lart -G'
alias l='ls -CFxaG'
alias m="java mocha.Decompiler"
alias mn=makensis
alias .b='. ~/.bashrc'
alias b='vi ~/.bashrc;.b'
alias .p='. ~/.profile'
alias p='vi ~/.bash_profile;.p'
alias pipi="pip install --install-option='--prefix=$HOME/local'"
alias pipu="pip uninstall"
alias vr="vi README*" 
alias x="chmod +x"
alias x.='chmod +x \$_'
alias find.="find . -name"
alias less="less -N"
alias q="vi ~/bin/.load_prerequisites"
alias s=store
alias wn="route get default | grep interface"
alias t1="tree -L 1 -a -p"
alias t2="tree -L 2 -a -p"
alias t3="tree -L 3 -a -p"
alias t4="tree -L 4 -a -p"
alias getw="curl https://api.weather.gov/gridpoints/OKX/33,35/forecast"
alias getf="curl https://api.weather.gov/gridpoints/OKX/33,35/forecast | jq '.properties.periods[0].detailedForecast'"
alias getp="curl https://api.weather.gov/gridpoints/OKX/33,35/forecast | jq .properties.periods[0].detailedForecast | sed  's/pre//'"
alias gw="curl http://api.worldweatheronline.com/premium/v1/weather.ashx?key=df7aa36af67145308e873424182212&q=new+york"
alias accw="curl http://apidev.accuweather.com/currentconditions/v1/335315.json?apikey= apikey=3nd45BH6lq4VXtHyLnYCQVk1f4lq15O1" 
alias accl="curl https://www.accuweather.com/en/us/new-york-ny/10007/current-weather/349727?lang=en-us&apikey=3nd45BH6lq4VXtHyLnYCQVk1f4lq15O1" 
title () {
	echo -n "\033]0;$1\007"
}

precmd() { DISP=$( echo "$PWD" | sed 's%^.*/\([^/]*$\)%\1%' ); eval "PS1='$DISP> '" }

v() { history | tac | egrep "vi " | sed -n 1p | zsh }
