trap "echo FAILED!; exit" ERR
set -x

arcyon='../../bin/arcyon'

id="$($arcyon create-revision -t title -p plan -f diff1)"
$arcyon get-diff -r $id --ls
$arcyon update-revision $id update -f diff2
$arcyon get-diff -r $id --ls

$arcyon query --format-type ids | grep $id

diffid="$($arcyon raw-diff diff1)"
diffid2="$($arcyon raw-diff diff2)"
$arcyon get-diff -d $diffid --ls
$arcyon get-diff -d $diffid2 --ls
id2="$($arcyon create-revision -t title2 -p plan --diff-id $diffid)"
$arcyon update-revision $id2 update --diff-id $diffid2

$arcyon query --format-type ids | grep $id2

$arcyon comment $id2 -m 'hello there!'
