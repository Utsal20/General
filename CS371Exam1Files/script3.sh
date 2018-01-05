echo "Enter number of classes:"
declare -i n
declare -i count=1
declare -i sumcredit=0
read n
while [ $count -le $n ]
do
	echo "Enter credits for subject $count:"
	declare -i eachcredit
	read eachcredit
	sumcredit=$(($sumcredit+$eachcredit))
	count=$(($count+1))
done
echo
echo "Enter name of most demanding class:"
read demanding_class
echo "Enter name of easiest class:"
read easiest_class
echo
echo "-------------------------------------------"
echo "Easiest class: $easiest_class"
echo "Most demanding class: $demanding_class"
echo "Total anticipated credits: $sumcredit"

