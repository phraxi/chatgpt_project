import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

# followed the tutorial from moropheus
# https://www.youtube.com/watch?v=u6V69py5Aps&list=PLNmsVeXQZj7rx55Mai21reZtd_8m-qe27&index=6
class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.lin1 = nn.Linear(10,10)
        self.lin2 = nn.Linear(10,10)

    def forward(self, x):
        x = F.relu(self.lin1(x))
        x = self.lin2(x)
        return x
    def num_flat_features(self, x):
        size = x.size()[1:]
        num = 1
        for i in size:
            num *= i
        return num

def main():
    net= MyNet()
    print(net)
    input = Variable(torch.randn(10,10))
    print(input)
    out = net(input)
    print(out)

if __name__ == "__main__":
    main()

