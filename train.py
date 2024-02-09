import torch
import torch.nn as nn
from torch.nn import functional as F



with open('input.text','r',encoding='utf-8') as f:
    text=f.read()



data= torch.tensor(encode(text),dtype=torch.long)

n= int(0.9*n)


class GPTLAnguageModel(nn.Module):
    def __init__(self):


    def _init_weight(self):

    def forward(self):


    def generate(self):





