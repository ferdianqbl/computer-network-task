#ab -n jumlah_request -c jumlah_konkuren http://localhost:8887/testing
#ab -n jumlah_request -c jumlah_konkuren http://localhost:8887/testing.txt


ab -n 1000 -c 10 http://localhost:8889/testing.txt
# ab -n 1000 -c 50 http://localhost:8889/testing.txt
# ab -n 1000 -c 100 http://localhost:8889/testing.txt
# ab -n 1000 -c 150 http://localhost:8889/testing.txt
# ab -n 1000 -c 200 http://localhost:8889/testing.txt
# abs -n 100 -c 1 https://localhost:8889/testing.txt
# abs -n 100 -c 10 https://www.apache.org/
# abs -l -n 5 https://www.google.com/

