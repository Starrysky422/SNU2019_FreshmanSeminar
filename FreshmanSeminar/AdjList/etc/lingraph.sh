for ((i=0;i<$1;i++)); do
	let "j = $i + 1"
	echo $i $j
done
