# do tests in order of time to execute
set -e # exit immediately on error

# cd to the dir of this script, so we can run scripts in the same dir
cd "$(dirname "$0")"

libscripts="$(find py -iname '*.py')"

# unittest
# 'sudo apt-get install python-nose' or use the commented-out version
# 'sudo apt-get install python-coverage' to use the '--with-coverage' option
# the '--with-profile' option should just work
# the '--failed' option will run only the tests that failed on the last run
PYTHONPATH=py/phl nosetests $libscripts --with-doctest --doctest-tests
#python -m unittest discover -p "*.py"

# N.B. can easily run individual tests with nose like so:
# nosetests abdcmd_default:TestAbd.test_abandonedWorkflow
