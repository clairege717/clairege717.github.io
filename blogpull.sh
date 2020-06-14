#! /bin/bash

result=$(cd ../Claire-Ge.github.io/Daily && git pull origin master | grep "Already up-to-date")
if [[ "$result" == "" ]]
then
  echo "`date '+%Y%m%d %H:%M'`:不需要更新代码"
  exit 0
else
  echo "`date '+%Y%m%d %H:%M'`:代码已经更新,开始"
  ps -ef|grep jekyll | awk '{print $2}'| sed -n '1,1p' | xargs -i kill {}
  rm -rf /root/_site
  jekyll serve -H '0.0.0.0' -s '/root/blog' >/dev/null 2>&1 &
fi