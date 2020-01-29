tar -czvf iQueensu.tar.gz ./iqueensu-dev-build
if [ "${CIRCLE_BRANCH}" = "dev-deploy" ];
then
  scp ./iQueensu.tar.gz "${TEST_USER_NAME}"@"${TEST_SERVER}:~/";
  ssh "${TEST_USER_NAME}"@"${TEST_SERVER}" "
    docker stop \$(docker ps -a -q)
    docker rm \$(docker container ls -a | grep 'iqueensu_backend:latest_dev' | awk '{print \$1}')
    docker rmi \$(docker images | grep 'iqueensu_backend' | awk '{print \$3}')
    docker rmi
    [ -d './iqueensu-dev-build' ] && rm -rf ./iqueensu-dev-build;
    tar -xzvf iQueensu.tar.gz;
    rm ./iQueensu.tar.gz;
    cd ./iqueensu-dev-build
    sed -i 's/8000:8000/23432:8000/g' docker-compose.yml
  ";
else echo "Skipped";
fi;
