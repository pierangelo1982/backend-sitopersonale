



docker run --name personale-mysql -e MYSQL_ROOT_PASSWORD=alnitek82 -p 3306:3306 -d mysql:5.7

docker run --name personale-phpmyadmin -d --link personale-mysql:db -p 8081:80 phpmyadmin/phpmyadmin
