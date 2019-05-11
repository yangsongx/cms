#!/bin/bash

function deploy_cn() {
    # swarm.yaml here is dynamically generated, and SHOULD NEVER be modified
    echo 'NOT READY YET'
    docker stack deploy -c template.yaml hscloud --with-registry-auth
}

function deploy_cn_test() {
    deploy_cn
}


case "$1" in
  cn)
  deploy_cn
  ;;
  cn-test)
  deploy_cn_test
  ;;
esac

