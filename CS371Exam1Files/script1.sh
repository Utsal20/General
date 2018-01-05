#dd if=/dev/urandom of=file1.txt bs=10 count=10
#dd if=/dev/urandom of=file2.txt bs=10 count=10
echo "Active processes"
echo "-------------------------------------------"
ps
echo "Everything in the current working directory"
echo "-------------------------------------------"
ls -a
echo "Combined result"
echo "-------------------------------------------"
cat file1 file2
echo "Path to current working directory"
echo "-------------------------------------------"
pwd
