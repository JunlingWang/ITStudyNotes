# Documentations 
[BeefLedger Community Documentation](https://hackmd.io/5g3l7aaXR-SfTGjM1W1ljA?both)  
# Online Tutorials
[Ethereum Pet Shop -- Your First Dapp](https://www.trufflesuite.com/tutorials/pet-shop)  
[CryptoZombies Code School](https://cryptozombies.io/)  
[Using puppeth To Manually Create An Ethereum Proof Of Authority (Clique) Network On AWS](https://medium.com/@collin.cusce/using-puppeth-to-manually-create-an-ethereum-proof-of-authority-clique-network-on-aws-ae0d7c906cce)  
# Geth
[Geth](https://geth.ethereum.org/downloads/) is a Go language implementation of Ethereum blockchain.
# Setup a sealer's node
In a PoA blockchain network, there are different types of nodes, including controllers, sealers, etc.  
To setup a sealer's node in AWS:  
1. Install a Ubuntu 16 on an EC2 instance, with username "ubuntu", and with the same keypair of the controller. store the private key, and upload the public key while launching the instance. The security group should be set as the online Puppeth instruction above.  
2. Set an elastic IP.  
3. Login to the instance through SSH, and run the following commands:  
sudo apt-get update  
sudo apt-get upgrade  
sudo apt-get install linux-image-extra-4.4.0–59-generic linux-image-extra-virtual  
sudo apt-get install \  
 apt-transport-https \  
 ca-certificates \  
 curl \  
 software-properties-common  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
sudo apt-key fingerprint 0EBFCD88  
sudo add-apt-repository \  
 “deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
 $(lsb_release -cs) \  
 stable”  
sudo apt-get update  
sudo apt-get install docker-ce  
sudo apt-get install docker-compose  
  
sudo groupadd docker  
sudo usermod -aG docker $USER  
  
4. Stop and restart the instance, run: "docker ps", and you can find the container ID and other information.  
  
The sealer's node is successfully set up.  
At this point, you can send your IP address to the controller, and they can add you to the network.  
  
# Operating a sealer's node
## Log into the node
docker exec -it containerID geth attach ipc:/root/.ethereum/geth.ipc  
## Get enode address  
admin.nodeInfo.enode  
## connect to other peers
admin.addPeer("enode address here")  

