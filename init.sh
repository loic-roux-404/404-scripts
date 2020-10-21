# TODO install deps from env (linux / darwin)
yarn global add auto

GH_TOKEN=${GH_TOKEN} auto create-labels
# TODO argparse
curl -fsL ${PRJ} > boilerplateProj.sh
chmod +x && ./boilerplateProj.sh $@
rm -rf ./boilerplateProj.sh

yarn global remove auto
