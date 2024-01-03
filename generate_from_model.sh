#!/bin/bash
rm -rf swagger-codegen-tmp || true
docker run --rm -v ${PWD}:/working swaggerapi/swagger-codegen-cli-v3:3.0.40 generate -i working/api.yml -l python-flask -o working/swagger-codegen-tmp
rm -rf swagger-codegen
mv swagger-codegen-tmp swagger-codegen
rm -rf ./swagger_server/models
cp ./swagger-codegen/swagger_server/swagger/swagger.yaml ./swagger_server/swagger
cp -r ./swagger-codegen/swagger_server/models ./swagger_server
cp -r ./swagger-codegen/.swagger-codegen ./swagger_server