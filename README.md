# GBTC

Electronic voting machines have been in existence for the past few years, and their security is guaranteed by a mix of electrical and mechanical approaches to solve the issue of anonymous voting. The problem faced is that these EVMs are not reconfigurable or connected to a network, making them both secure and almost impossible to handle information transfer. For people of the same constituency, the EVMs in existence work just fine, but to vote, people have to travel to their constituency.


To fix this we introduce another digital EVM which is reconfigurable, and meant only for people not currently in their constituency. The EVM will be kept separately and will be connected to a decentralised network, containing information about out-of-constituency voters and candidates. The chain also consists of nodes pointing to the EVMs, which vouch for their validation. The node consists of information such as “valid value”. To further explain, each EVM will have a “critical section”, these sections will be in charge of certain functions of a voting machine, such as counting votes, VVPAT, loading candidate list and so on. These sections are also in charge of coming up with a checksum. With each vote, the value is generated and compared to the valid value in the node the machine is linked to. This value must always match the value on the node, if not, the machine is said to be compromised. Thus the machine can be reset or changed if found faulty. This gives the advantage that the system not only detects faults in the EVM, but can fix them as well. This also makes these new EVMs secure, and  flexible as well.
The validation of voters voting on this EVM can be done via a simple app that checks the chain for information, similar to how regular voters are validated on voting day. After voting has concluded, the EVM connected to the blockchain can also transmit information such as the number of votes from that EVM to the right place, automating the process and minimising the hassle of counting the out of constituency votes.

## Setup

### Prerequisites

1. Run `cd azure-vote\`
2. Run `npm install`
3. Run `pip3 install flask flask-cors requests`

### EVM

1. Run `python3 app.py`
2. Run index.html (either as a deployement or on a server).
