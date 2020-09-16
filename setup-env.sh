#!/bin/bash

# 
# for library specific requiremtns, see README of each repo
#

EXPDIR=$PWD

# libraries
MOSES=https://github.com/moses-smt/mosesdecoder.git
SENT_PIECE='sentencepiece==0.1.8'
TENSORFLOW='tensorflow-gpu==1.4.1'
#OPENNMT=https://github.com/OpenNMT/OpenNMT-tf/tree/v1.15.0 # install updated version ./OpenNM

# Data, Processing
if [ ! -d $EXPDIR/mosesdecoder ]; then
  echo "Cloning Mosesdecoder ..."
  git clone $MOSES
fi

echo "Installing SentencePiece ..."
pip install $SENT_PIECE


# NMT
echo "Install tensorflow.."
pip install $TENSORFLOW

if [ -d $EXPDIR/OpenNMT ]; then
  cd ./OpenNMT
  pip install -e ./ 
fi

echo "Install CUDA 8"

wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb
dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb

apt-key add /var/cuda-repo-8-0-local-ga2/7fa2af80.pub
apt-get update
apt-get install cuda=8.0.61-1
apt autoremove
