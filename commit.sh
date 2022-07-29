msg=$1
git add .
git status
git commit -m "$msg"
git push
