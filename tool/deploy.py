import os

import requests
import json


# 配置信息
# docker仓库地址
DOCKER_ADDRESS = "xu756-docker.pkg.coding.net/me/imlogic/"
# 部署的镜像名称
DOCKER_IMAGE_NAME = os.environ.get("DOCKER_IMAGE_NAME")
# 部署的镜像版本
DOCKER_IMAGE_VERSION = os.environ.get("DOCKER_IMAGE_VERSION")


def deploy():
    headers = {
        "content-type": "application/json",
        "Cookie": "KuboardUsername=admin; KuboardAccessKey=hj5tx7ax78df.4kfhtd7bswcji6p4e2hjstnzaihk2byw"
    }

    # 构造请求体
    data = {
        "kind": "deployments",
        "namespace": "app",
        "name": DOCKER_IMAGE_NAME,
        "images": {
            DOCKER_ADDRESS + DOCKER_IMAGE_NAME:
                DOCKER_ADDRESS + DOCKER_IMAGE_NAME + ":" + DOCKER_IMAGE_VERSION
        }
    }

    # 发送请求
    url = "http://121.5.132.57:7087/kuboard-api/cluster/xu756-product/kind/CICDApi/admin/resource/updateImageTag"
    response = requests.put(url, headers=headers, data=json.dumps(data))

    # 打印响应
    print(response.text)


if __name__ == '__main__':
    deploy()
