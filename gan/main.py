"""
To run Instructor
"""
import argparse
from instructor import Instructor

parser = argparse.ArgumentParser(description='')
parser.add_argument('-bert_model', type=str, default='', help='bert model string')
parser.add_argument('-general_in', type=str, default='', help='path to general_in* file')
parser.add_argument('-maxlen', type=int, default='',help='max sequence length')
parser.add_argument('-batch_size', type=int, default='',help='')
parser.add_argument('-epochs', type=int, default='',help='number of iterations')
parser.add_argument('-model_out', type=str, default='', help='path to model dir')
parser.add_argument('-result_out', type=str, default='', help='path to result dir')
parser.add_argument("-cuda", action="store_true", help="use gpu or not")

args = parser.parse_args()
print(args)

instructor = Instructor(args)
instructor.train()