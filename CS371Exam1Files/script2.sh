echo "Enter a child's age:"
declare -i age
read age
echo "Appropriate toy:"
if [ $age -lt 4 ]
then
echo $1
elif [ $age -lt 8 ]
then
echo $2
else
echo $3
fi
echo "-------------------------------------------"
echo "Enter your birthday month number (1-12):"
declare -i month
read month
echo "Corresponding month:"
case $month in
1 ) echo "January";;
2 ) echo "February";;
3 ) echo "March";;
4 ) echo "April";;
5 ) echo "May";;
6 ) echo "June";;
7 ) echo "July";;
8 ) echo "August";;
9 ) echo "September";;
10 ) echo "October";;
11 ) echo "November";;
12 ) echo "December";;
esac
